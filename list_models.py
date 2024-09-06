import openai

def list_models(api_key):
    openai.api_key = api_key
    try:
        models = openai.Model.list()
        for model in models['data']:
            print(f"Model ID: {model['id']}, Model Object: {model['object']}")
    except Exception as e:
        print(f"Error while listing models: {e}")

if __name__ == "__main__":
    import os
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Please set the OPENAI_API_KEY environment variable.")
    else:
        list_models(api_key)
