📰 News Intelligence RAG System - NewsBuddy — Product Requirements Document (PRD)
1. 📌 Overview
1.1 Product Name

NewsBuddy

1.2 Objective

Develop a domain-specific Retrieval-Augmented Generation (RAG) system that:

Ingests AI and technology news articles daily
Enables natural language querying
Produces accurate, time-aware, citation-grounded responses
2. 🎯 Goals & Success Criteria
2.1 Primary Goals
Deliver highly relevant AI/tech news insights
Ensure low hallucination via grounded retrieval
Maintain daily data freshness
Achieve < 3 seconds response latency
2.2 Success Metrics
Metric	Target
Precision@K	≥ 0.7
Answer correctness	High (manual eval)
Latency	< 3s
Data freshness	≤ 24h delay
3. 👤 Target Users
Primary Audience
ML/AI students and engineers
Tech enthusiasts
Researchers tracking industry trends
4. 🧩 Core Features
4.1 Natural Language Query Interface

Users can ask:

“What happened in AI this week?”
“Latest news about large language models”
“Recent developments in computer vision”
4.2 Retrieval-Augmented Answer Generation
Hybrid retrieval (semantic + keyword)
Context-grounded answer generation
Responses include source attribution
4.3 Time-Aware Retrieval (Explicit Filtering)
Parse temporal expressions:
“today”
“this week”
“last 3 days”
Apply metadata-based filtering before retrieval
4.4 Daily Data Ingestion Pipeline
Batch ingestion every 24 hours
Incremental updates to vector database
4.5 Source Attribution

Each response includes:

Article title
Source name
Publication date
4.6 Deduplication System (Embedding-Based)
Compute similarity between articles
Remove near-duplicates using similarity threshold
4.7 Topic Categorization
Use categories provided by News API
Filter AI/Tech-related articles
5. 🏗️ System Architecture
5.1 High-Level Components
News Ingestion Service
Preprocessing Pipeline
Embedding Generator (Sentence-Transformers)
Vector Database (Pinecone)
Hybrid Retrieval Engine
LLM Generation Layer (OpenAI)
Streamlit UI
5.2 Data Flow
[News API]
   ↓
[Raw Articles]
   ↓
[Preprocessing + Deduplication]
   ↓
[Chunking (Hybrid)]
   ↓
[Embeddings]
   ↓
[Pinecone Vector DB]
   ↓
[User Query]
   ↓
[Date Filtering + Hybrid Retrieval]
   ↓
[LLM Generation]
   ↓
[Answer + Citations]
6. ⚙️ Technical Specifications
6.1 Data Source
NewsAPI (primary source)
Filter by:
Keywords: “AI”, “machine learning”, “technology”
Categories: technology
6.2 Preprocessing
Remove boilerplate text
Normalize timestamps
Deduplicate using embedding similarity
6.3 Chunking Strategy (Hybrid)
Split by paragraph boundaries
Enforce max token size (~300–500 tokens)
Maintain semantic coherence
6.4 Embeddings
Model: Sentence-Transformers (local inference)
Store:
Embedding vectors
Metadata (date, source, topic)
6.5 Vector Storage
Pinecone
Index includes:
Embeddings
Metadata filters (timestamp, category)
6.6 Retrieval Strategy (Hybrid)
Step 1: Filtering
Apply date constraints
Apply category filters (AI/tech)
Step 2: Retrieval
Semantic similarity search
Keyword matching (BM25 or equivalent)
Step 3: Combine Scores
Weighted hybrid scoring
6.7 Reranking (Planned Future Enhancement)
Cross-encoder reranker (to be added later)
6.8 LLM Generation
OpenAI model (e.g., GPT-4 class)
Prompt Requirements:
Restrict to retrieved context
Enforce citation usage
Avoid hallucination
7. 🖥️ Frontend (Streamlit UI)
Features
Chat-style query interface
Display:
Generated answer
Supporting articles
Optional filters:
Date range
Topic
8. 🔄 Non-Functional Requirements
Performance
Response time: < 3 seconds
Scalability
Handle 10k–50k articles
Reliability
Graceful handling of API failures
9. 📊 Evaluation Plan
Dataset
Curated set of queries:
“Latest AI breakthroughs”
“Recent OpenAI announcements”
“Tech layoffs this month”
Metrics
Precision@K (retrieval quality)
Answer correctness (manual scoring)
Latency tracking
10. 🚀 Development Roadmap
Week 1
News API ingestion
Basic preprocessing
Initial RAG pipeline (semantic search only)
Week 2
Hybrid retrieval
Time filtering
Deduplication
Streamlit UI
Week 3 (Enhancement Phase)
Evaluation pipeline
Optimization (latency, filtering)
UI improvements
11. ⚠️ Risks & Mitigation
Risk	Mitigation
Duplicate articles	Embedding similarity filtering
Irrelevant results	Hybrid retrieval
Outdated info	Daily ingestion
Hallucination	Strict grounding prompts
12. 📌 Future Enhancements
Reranking (cross-encoder)
Topic clustering
Trending topic detection
Personalized feeds
Real-time ingestion upgrade