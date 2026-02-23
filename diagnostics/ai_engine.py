# AI Diagnostic Engine — OpenAI Integration
#
# This module handles the AI-powered diagnostic logic.
# It sends pet symptoms to the OpenAI API and returns
# preliminary clinical suggestions for veterinarian review.

import os


def get_ai_diagnosis(symptoms: str, pet_species: str = '', pet_breed: str = '') -> dict:
    """
    Send pet symptoms to OpenAI and return diagnostic suggestions.

    Args:
        symptoms: Description of the pet's symptoms
        pet_species: e.g. 'dog', 'cat'
        pet_breed: e.g. 'Labrador', 'Persian'

    Returns:
        dict with 'suggestions' list and 'disclaimer' string
    """
    # TODO: Implement OpenAI API call
    # from openai import OpenAI
    # client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    #
    # response = client.chat.completions.create(
    #     model="gpt-4",
    #     messages=[{
    #         "role": "system",
    #         "content": "You are a veterinary clinical decision support tool..."
    #     }, {
    #         "role": "user",
    #         "content": f"Species: {pet_species}, Breed: {pet_breed}, Symptoms: {symptoms}"
    #     }]
    # )

    return {
        'suggestions': [],
        'disclaimer': (
            'This is an AI-generated preliminary assessment for veterinary review only. '
            'It does not constitute a final diagnosis. All AI-generated insights must be '
            'validated by a licensed veterinarian.'
        ),
    }
