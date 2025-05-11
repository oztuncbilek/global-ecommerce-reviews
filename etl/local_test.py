from pyspark.sql import SparkSession
from transformers import pipeline
import time

spark = SparkSession.builder \
    .appName("LocalSentimentAnalysis") \
    .master("local[4]") \  
    .config("spark.driver.memory", "4g") \
    .getOrCreate()


df = spark.read.csv("data/sample/reviews_sample.csv", header=True, escape='"')

def analyze_sentiment(text):
    try:
        analyzer = pipeline("sentiment-analysis", 
                          model="distilbert-base-uncased-finetuned-sst-2-english",
                          device=-1) 
        return analyzer(text[:512])[0]['label']
    except:
        return "neutral"

start_time = time.time()
sample = df.limit(100).toPandas()  
sample['sentiment'] = sample['review_text'].apply(analyze_sentiment)
print(f"Execution time: {time.time() - start_time:.2f} seconds")

print(sample[['review_text', 'sentiment']].head(10))

spark.stop()