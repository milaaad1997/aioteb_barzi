from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    df = pd.read_csv('signs_t.csv', index_col=0)
    signs = list(df.columns[:10])  # Only take the first 10 signs
    return render_template('index.html', signs=signs, show_symptoms=True)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    df = pd.read_csv('signs_t.csv', index_col=0)
    df_user = pd.DataFrame(index=df.index)

    for sign in df.columns[:10]:  # Only take the first 10 signs
        answer = request.form.get(sign)  # Get the answer from the form
        df_user[sign] = df[sign]
        df_user.loc['user', sign] = answer

    df_user.to_csv('signs_u.csv')

    data = pd.read_csv('signs_u.csv')
    data.set_index(data.columns[0], inplace=True)
    data = data.astype(float)

    csim = cosine_similarity(data)
    sim_df = pd.DataFrame(csim, index=data.index, columns=data.index)

    sorted_similarities = sim_df['user'].sort_values(ascending=False)
    sorted_similarities = (sorted_similarities * 100).drop('user')

    results = []
    for index, value in sorted_similarities.items():
        results.append((f'{value:.2f}%', index))

    max_similarity = sorted_similarities.max()
    if max_similarity < 40:
        results.append(('کاربر سالم است.', ''))
    elif 40 <= max_similarity < 70:
        results.append((f'کاربر مریض است. بیماری ممکن: {sorted_similarities.idxmax()}', ''))
    else:
        results.append((f'کاربر باید به پزشک مراجعه کند. بیماری ممکن: {sorted_similarities.idxmax()}', ''))

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)




