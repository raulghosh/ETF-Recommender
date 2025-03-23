from openai import OpenAI
import json
from pathlib import Path

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_etf_data(prompt_path, output_dir):
    prompt = Path(prompt_path).read_text()
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a financial data expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        response_format={"type": "json_object"}
    )
    
    output_path = Path(output_dir) / f"etf_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    with open(output_path, "w") as f:
        json.dump(json.loads(response.choices[0].message.content), f)
    
    return output_path