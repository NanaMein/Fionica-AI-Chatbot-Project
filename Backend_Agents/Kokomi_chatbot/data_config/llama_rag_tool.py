from typing import Any
from crewai.project import tool
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.text_splitter import SentenceSplitter
from ..llm_config.llm_models import rag_llm as llm

embed_model=HuggingFaceEmbedding()
llm=llm()

from crewai_tools import LlamaIndexTool
from functools import lru_cache

@lru_cache(maxsize=1)  # Ensures this only runs once globally
def initialize_rag_pipeline():
    # Load and process documents (runs only once)
    load_documents = SimpleDirectoryReader(input_dir='data_storage_sources').load_data()
    chunking = SentenceSplitter(chunk_size=800, chunk_overlap=100)
    nodes = chunking.get_nodes_from_documents(load_documents)
    index = VectorStoreIndex(embed_model=embed_model, nodes=nodes)
    return index.as_query_engine(llm=llm)  # Return the query engine

def create_kokomi_tool():
    # Reuses the cached query engine
    query_engine = initialize_rag_pipeline()
    return LlamaIndexTool.from_query_engine(
        query_engine=query_engine,
        name="kokomi_rag_tool",
        description="A RAG tool for querying Kokomi-related documents"
    )


#/*/*/*/*/*///***///***///****///****////*********///////******/////******//***//
# from functools import lru_cache
#
# @lru_cache(maxsize=1)
# def kokomi_rag_tool():
#     load_documents = SimpleDirectoryReader(input_dir='data_storage_sources').load_data()
#
#     chunking = SentenceSplitter(chunk_size=800, chunk_overlap=100)
#
#     nodes = chunking.get_nodes_from_documents(load_documents)
#
#     index = VectorStoreIndex(embed_model=embed_model,nodes=nodes)
#
#     query_engine = index.as_query_engine(llm=llm)
#
#     return LlamaIndexTool.from_query_engine(
#         name="kokomi_rag_tool",
#         description="A RAG tool for querying Kokomi-related documents",
#         query_engine=query_engine
#     )
#****************************////////////*******//////*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
    # @tool("rag tool")
    # def kokomi_tool(question: str) -> str:
    #     response_obj = query_engine.query(f"""You will cosplay and roleplay as Kokomi,
    #                 and your scenario and place would be in the island. You will answer based on //{question}//
    #                 """)
    #
    #     response_str = response_obj.response
    #     return response_str
    #
    # return kokomi_tool

