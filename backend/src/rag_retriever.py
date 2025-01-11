import os

class RAGRetriever:
    def __init__(self):
        self.documents = []
        self.load_docs()

    def load_docs(self):
        file_path = "/app/docs/sample-docs/my-sample.txt"

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
            self.documents.append(text)
            print(f"Loaded doc from {file_path}")
        else:
            print(f"File {file_path} not found. Skipping doc load.")

    def get_relevant_docs(self, query: str):
        print(f"[RAGRetriever] Returning docs from my-sample.txt for query: {query}")
        return self.documents
