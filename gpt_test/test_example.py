from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.dataset import EvaluationDataset
from deepeval.metrics import HallucinationMetric, AnswerRelevancyMetric


'''def test_answer_relevancy():
    answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.5)
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        # Replace this with the actual output of your LLM application
        actual_output="We offer a 30-day full refund at no extra cost.",
        retrieval_context=["All customers are eligible for a 30 day full refund at no extra cost."]
    )
    assert_test(test_case, [answer_relevancy_metric])   
'''

"""data = [
    {
        "input": "What is the capital of France?",
        "expected_output": "Paris",
        "context": ["France is a country in Europe."]
    },
    {
        "input": "What is 2 + 2?",
        "expected_output": "4"
    },
    # Add more data points as needed
]

test_cases = [
    LLMTestCase(
        input=item["input"],
        expected_output=item["expected_output"],
        context=item.get("context", [])
    )
    for item in data
]

dataset = EvaluationDataset(test_cases=test_cases)

dataset.save("my_first_dataset.json")


"""


from openai import OpenAI
client = OpenAI()

def get_completion(prompt, client_instance, model='gpt-3.5-turbo'):
  messages = [{'role': 'user', 'content': prompt}]
  response = client_instance.chat.completions.create(
  model=model,
  messages=messages,
  max_tokens=50,
  temperature=0.6,
  )
  return response.choices[0].message.content

#print(get_completion('hello', client) )# call your function


data = [
    {
        "input": "What permits do I need for a kitchen remodel?",
        "expected_output": "For a kitchen remodel, you'll typically need building permits covering electrical, plumbing, and structural changes. It's essential to check with your local building department for specific requirements.",
        "context": [
            "The client is planning a kitchen renovation.",
            "Local regulations may vary regarding required permits."
        ]
    },
    {
        "input": "How long does a bathroom renovation usually take?",
        "expected_output": "A standard bathroom renovation typically takes about 2 to 3 weeks, depending on the project's complexity and unforeseen issues.",
        "context": [
            "The client is considering renovating their bathroom.",
            "Timeline can vary based on factors like material availability and contractor schedules."
        ]
    },
    {
        "input": "What are the benefits of using energy-efficient windows?",
        "expected_output": "Energy-efficient windows can reduce energy bills, improve indoor comfort, and increase your home's value by minimizing heat loss and gain.",
        "context": [
            "The client is exploring window replacement options.",
            "Energy efficiency is a priority for the client."
        ]
    },
    {
        "input": "Can I live in my house during the renovation?",
        "expected_output": "Living in your house during renovation is possible but may be challenging due to noise, dust, and limited access to certain areas. It's important to discuss this with your contractor to ensure safety and feasibility.",
        "context": [
            "The client is concerned about staying in their home during the renovation.",
            "The extent of the renovation impacts the livability of the home."
        ]
    },
    {
        "input": "What should I consider when hiring a contractor?",
        "expected_output": "When hiring a contractor, consider their experience with similar projects, check references, verify licensing and insurance, and ensure clear communication about timelines and costs.",
        "context": [
            "The client is seeking guidance on selecting a contractor.",
            "Trustworthiness and reliability are key concerns for the client."
        ]
    }
]



for item in data:
    item['actual_output'] = get_completion(item['input'], client)



test_cases = [
    LLMTestCase(
        input=item['input'],
        expected_output=item['expected_output'],
        actual_output=item['actual_output'],
        context=item['context']
    )
    for item in data
]

#print(test_cases)

dataset = EvaluationDataset(test_cases=test_cases)

hallucination_metric = HallucinationMetric(threshold=0.3)
answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.5)

dataset.evaluate([hallucination_metric, answer_relevancy_metric])

