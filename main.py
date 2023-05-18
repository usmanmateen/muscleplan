from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/generate_workout', methods=['POST'])
def generate_workout():
    user_inputs = request.form  # Assuming you're using a form to capture user inputs

    # Extract user inputs
    age = user_inputs.get('age')
    weight = user_inputs.get('weight')
    height = user_inputs.get('height')
    goals = user_inputs.get('goals')

    # Generate workout plan using the ChatGPT API
    prompt = f"Age: {age}\nWeight: {weight}\nHeight: {height}\nGoals: {goals}"
    response = openai.Completion.create(
        engine='davinci-codex',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None
    )
    workout_plan = response.choices[0].text.strip()

    # Return the generated workout plan as a JSON response
    return jsonify({'workout_plan': workout_plan})


if __name__ == '__main__':
    app.run(debug=True)
