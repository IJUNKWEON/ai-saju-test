
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    return jsonify({
        "reply": """
[테스트 응답 예시]
1) 성격: 차분하고 이성적인 판단력이 뛰어나며, 타인의 감정을 잘 헤아립니다.
2) 직업운: 기획, 상담, IT 분야에 적성이 맞고 장기적인 관점에서 안정적 성장 가능.
3) 재물운: 자산을 안정적으로 관리하며 갑작스런 투자보다는 저축 중심이 유리.
4) 연애운: 신중하며 오래가는 관계를 선호하며, 중후반기에 좋은 인연이 들어옵니다.
5) 건강운: 소화기계통에 주의가 필요하며, 평소 꾸준한 운동이 중요합니다.
6) 대운 흐름: 2027년부터 대운의 전환이 있으며 직업/인간관계에 큰 변화가 예상됩니다.
7) 연도별 흐름: 2025년 안정 / 2026년 주의 / 2027~2030년 상승운으로 전환됩니다.
8) 전체 인생운: 40대 이후 운세가 크게 상승하며, 후반기로 갈수록 운이 강해집니다.
"""
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
