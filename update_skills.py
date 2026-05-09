import re

def replace_skills(filepath, lang='en'):
    with open(filepath, 'r') as f:
        content = f.read()

    if lang == 'en':
        new_skills = """        <div class="skill-category">
          <div class="skill-category-header">
            <span class="skill-icon">💻</span>
            <h3 class="skill-title">Programming Languages</h3>
          </div>
          <div class="skill-tags">
            <span class="skill-tag">Python</span>
            <span class="skill-tag">C#</span>
            <span class="skill-tag">Java</span>
            <span class="skill-tag">C/C++</span>
            <span class="skill-tag">SQL</span>
            <span class="skill-tag">Bash/Shell</span>
            <span class="skill-tag">HTML</span>
          </div>
        </div>

        <div class="skill-category">
          <div class="skill-category-header">
            <span class="skill-icon">🤖</span>
            <h3 class="skill-title">AI/ML &amp; NLP</h3>
          </div>
          <div class="skill-tags">
            <span class="skill-tag">PyTorch</span>
            <span class="skill-tag">TensorFlow/Keras</span>
            <span class="skill-tag">scikit-learn</span>
            <span class="skill-tag">Hugging Face Transformers</span>
            <span class="skill-tag">Transfer Learning</span>
            <span class="skill-tag">RAG</span>
            <span class="skill-tag">Semantic Search</span>
            <span class="skill-tag">LLM APIs &amp; Prompt Engineering</span>
            <span class="skill-tag">NLTK</span>
            <span class="skill-tag">Gensim</span>
          </div>
        </div>

        <div class="skill-category">
          <div class="skill-category-header">
            <span class="skill-icon">🔬</span>
            <h3 class="skill-title">Domain &amp; Research</h3>
          </div>
          <div class="skill-tags">
            <span class="skill-tag">Cyber-Physical Systems</span>
            <span class="skill-tag">Reinforcement Learning</span>
            <span class="skill-tag">Time-Series Forecasting</span>
          </div>
        </div>

        <div class="skill-category">
          <div class="skill-category-header">
            <span class="skill-icon">🗄️</span>
            <h3 class="skill-title">Data &amp; Databases</h3>
          </div>
          <div class="skill-tags">
            <span class="skill-tag">NumPy</span>
            <span class="skill-tag">Pandas</span>
            <span class="skill-tag">MySQL</span>
            <span class="skill-tag">MongoDB</span>
            <span class="skill-tag">ChromaDB</span>
            <span class="skill-tag">Weaviate</span>
            <span class="skill-tag">GraphQL</span>
            <span class="skill-tag">Data Preprocessing</span>
          </div>
        </div>

        <div class="skill-category">
          <div class="skill-category-header">
            <span class="skill-icon">📐</span>
            <h3 class="skill-title">Software Engineering</h3>
          </div>
          <div class="skill-tags">
            <span class="skill-tag">REST APIs</span>
            <span class="skill-tag">OOP Design Patterns</span>
            <span class="skill-tag">Modular Architecture</span>
            <span class="skill-tag">Agile (Scrum)</span>
            <span class="skill-tag">Git</span>
          </div>
        </div>

        <div class="skill-category">
          <div class="skill-category-header">
            <span class="skill-icon">🛠️</span>
            <h3 class="skill-title">Tools &amp; Platforms</h3>
          </div>
          <div class="skill-tags">
            <span class="skill-tag">Linux/Ubuntu</span>
            <span class="skill-tag">Docker</span>
            <span class="skill-tag">AWS</span>
            <span class="skill-tag">Streamlit</span>
            <span class="skill-tag">Jupyter</span>
            <span class="skill-tag">Figma</span>
          </div>
        </div>"""
        
        # Find the content between <div class="skills-grid"> and the last </div> before </section>
        pattern = re.compile(r'(<div class="skills-grid">\s*)(.*?)(^\s*</div>\s*</section>)', re.MULTILINE | re.DOTALL)
        content = pattern.sub(r'\1\n' + new_skills + r'\n\3', content)

    else:
        new_skills = """                <div class="skill-category">
                    <div class="skill-category-header">
                        <span class="skill-icon">💻</span>
                        <h3 class="skill-title">编程语言</h3>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">Python</span>
                        <span class="skill-tag">C#</span>
                        <span class="skill-tag">Java</span>
                        <span class="skill-tag">C/C++</span>
                        <span class="skill-tag">SQL</span>
                        <span class="skill-tag">Bash/Shell</span>
                        <span class="skill-tag">HTML</span>
                    </div>
                </div>

                <div class="skill-category">
                    <div class="skill-category-header">
                        <span class="skill-icon">🤖</span>
                        <h3 class="skill-title">AI / ML / NLP</h3>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">PyTorch</span>
                        <span class="skill-tag">TensorFlow/Keras</span>
                        <span class="skill-tag">scikit-learn</span>
                        <span class="skill-tag">Hugging Face Transformers</span>
                        <span class="skill-tag">Transfer Learning</span>
                        <span class="skill-tag">RAG</span>
                        <span class="skill-tag">Semantic Search</span>
                        <span class="skill-tag">LLM APIs &amp; Prompt Engineering</span>
                        <span class="skill-tag">NLTK</span>
                        <span class="skill-tag">Gensim</span>
                    </div>
                </div>

                <div class="skill-category">
                    <div class="skill-category-header">
                        <span class="skill-icon">🔬</span>
                        <h3 class="skill-title">研究领域</h3>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">Cyber-Physical Systems</span>
                        <span class="skill-tag">Reinforcement Learning</span>
                        <span class="skill-tag">Time-Series Forecasting</span>
                    </div>
                </div>

                <div class="skill-category">
                    <div class="skill-category-header">
                        <span class="skill-icon">🗄️</span>
                        <h3 class="skill-title">数据与数据库</h3>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">NumPy</span>
                        <span class="skill-tag">Pandas</span>
                        <span class="skill-tag">MySQL</span>
                        <span class="skill-tag">MongoDB</span>
                        <span class="skill-tag">ChromaDB</span>
                        <span class="skill-tag">Weaviate</span>
                        <span class="skill-tag">GraphQL</span>
                        <span class="skill-tag">Data Preprocessing</span>
                    </div>
                </div>

                <div class="skill-category">
                    <div class="skill-category-header">
                        <span class="skill-icon">📐</span>
                        <h3 class="skill-title">软件工程</h3>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">REST APIs</span>
                        <span class="skill-tag">OOP Design Patterns</span>
                        <span class="skill-tag">Modular Architecture</span>
                        <span class="skill-tag">Agile (Scrum)</span>
                        <span class="skill-tag">Git</span>
                    </div>
                </div>

                <div class="skill-category">
                    <div class="skill-category-header">
                        <span class="skill-icon">🛠️</span>
                        <h3 class="skill-title">工具与平台</h3>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">Linux/Ubuntu</span>
                        <span class="skill-tag">Docker</span>
                        <span class="skill-tag">AWS</span>
                        <span class="skill-tag">Streamlit</span>
                        <span class="skill-tag">Jupyter</span>
                        <span class="skill-tag">Figma</span>
                    </div>
                </div>"""
        
        pattern = re.compile(r'(<div class="skills-grid">\s*)(.*?)(^\s*</div>\s*</section>)', re.MULTILINE | re.DOTALL)
        content = pattern.sub(r'\1\n' + new_skills + r'\n\3', content)
        
    with open(filepath, 'w') as f:
        f.write(content)

replace_skills('index.html', 'en')
replace_skills('index-zh.html', 'zh')
print("Skills updated")
