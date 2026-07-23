<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MyStair - 마이스터고 AI 커리어 빌딩 플랫폼</title>
    <!-- 토스 스타일의 깔끔한 폰트 (Pretendard) -->
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.8/dist/web/static/pretendard.css" />
    <style>
        /* 기본 리셋 및 폰트 설정 */
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Pretendard', sans-serif; }
        body { background-color: #f2f4f6; color: #333d4b; line-height: 1.6; overflow-x: hidden; }

        /* 내비게이션 바 */
        header {
            display: flex; justify-content: space-between; align-items: center;
            padding: 20px 50px; position: sticky; top: 0;
            background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px);
            z-index: 100; border-bottom: 1px solid #e5e8eb;
        }
        .logo { font-size: 24px; font-weight: 800; color: #3182f6; text-decoration: none; letter-spacing: -0.5px; }
        .nav-links a { margin-left: 20px; text-decoration: none; color: #4e5968; font-weight: 600; font-size: 15px; transition: color 0.2s; }
        .nav-links a:hover { color: #191f28; }

        /* 히어로 섹션 */
        .hero { text-align: center; padding: 80px 20px 40px; background: #ffffff; animation: fadeInUp 0.8s ease-out; }
        .hero h1 { font-size: 48px; font-weight: 800; color: #191f28; margin-bottom: 20px; letter-spacing: -1px; line-height: 1.3; }
        .hero p { font-size: 20px; color: #6b7684; margin-bottom: 40px; font-weight: 500; }

        .btn-primary {
            background-color: #3182f6; color: white;
            padding: 18px 36px; border: none; border-radius: 14px;
            font-size: 18px; font-weight: 700; cursor: pointer;
            transition: all 0.2s ease; box-shadow: 0 4px 12px rgba(49,130,246,0.2);
        }
        .btn-primary:hover { background-color: #1b64da; transform: translateY(-2px); box-shadow: 0 6px 16px rgba(49,130,246,0.3); }
        .btn-primary:active { transform: scale(0.97); }

        /* 워크스페이스 컨테이너 */
        .workspace-container { max-width: 900px; margin: 40px auto; padding: 0 20px; animation: fadeInUp 1s ease-out 0.2s both; }

        /* 카드 공통 스타일 (토스 스타일) */
        .card {
            background: #ffffff; border-radius: 24px; padding: 30px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.03); margin-bottom: 30px;
            border: 1px solid #f0f0f6;
        }
        .card-header { font-size: 22px; font-weight: 700; color: #191f28; margin-bottom: 20px; display: flex; align-items: center; justify-content: space-between; }

        /* 기능 1: AI 목표 분해 입력창 */
        .goal-input-group { display: flex; gap: 10px; margin-bottom: 20px; }
        .goal-input-group input {
            flex: 1; padding: 18px; border: 1px solid #e5e8eb; border-radius: 12px;
            font-size: 16px; font-weight: 500; outline: none; background: #f9fafb;
        }
        .goal-input-group input:focus { border-color: #3182f6; background: #ffffff; }

        /* 태스크 리스트 */
        .task-list { display: flex; flex-direction: column; gap: 12px; }
        .task-item {
            display: flex; align-items: center; justify-content: space-between;
            background: #f9fafb; padding: 16px 20px; border-radius: 12px;
            transition: background 0.2s;
        }
        .task-item:hover { background: #f0f4f8; }
        .task-text { font-size: 16px; font-weight: 600; color: #333d4b; }
        .task-tag { font-size: 12px; font-weight: 700; color: #3182f6; background: #e8f3ff; padding: 4px 10px; border-radius: 6px; }

        /* 기능 2: 캘린더 업로드 & 태깅 결과 */
        .upload-area {
            border: 2px dashed #d1d6db; border-radius: 16px; padding: 40px 20px;
            text-align: center; cursor: pointer; background: #fafbfc; transition: border 0.2s;
            margin-bottom: 20px;
        }
        .upload-area:hover { border-color: #3182f6; }
        .upload-icon { font-size: 32px; margin-bottom: 10px; }
        .upload-text { font-size: 16px; font-weight: 600; color: #6b7684; }

        #visionResult { display: none; background: #e8f3ff; padding: 20px; border-radius: 12px; margin-top: 15px; border-left: 4px solid #3182f6; }
        .tag-pill { display: inline-block; background: #3182f6; color: white; padding: 6px 12px; border-radius: 20px; font-size: 13px; font-weight: bold; margin-right: 8px; margin-bottom: 8px;}

        /* 기능 3: 자소서 추출 결과 */
        #resumeResult { display: none; padding: 25px; border-radius: 16px; background: #f9fafb; border: 1px solid #e5e8eb; margin-top: 20px;}
        .resume-title { font-size: 18px; font-weight: bold; color: #191f28; margin-bottom: 15px; }
        .resume-content { font-size: 15px; color: #4e5968; line-height: 1.7; }
        .star-section { margin-bottom: 12px; }
        .star-label { font-weight: 700; color: #3182f6; margin-right: 8px; }

        /* 로딩 스피너 */
        .spinner {
            display: none; width: 20px; height: 20px; border: 3px solid rgba(49,130,246,0.2);
            border-top-color: #3182f6; border-radius: 50%; animation: spin 1s linear infinite; margin-left: 10px;
        }

        @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes spin { to { transform: rotate(360deg); } }
    </style>
</head>
<body>

    <header>
        <a href="#" class="logo">MyStair</a>
        <div class="nav-links">
            <a href="#">목표 분해</a>
            <a href="#">경험 캘린더</a>
            <a href="#">자소서 추출</a>
        </div>
    </header>

    <section class="hero">
        <h1>나의 실습 경험이<br>취업의 계단이 되다.</h1>
        <p>AI가 목표를 쪼개주고, 사진 한 장으로 실습을 자동 로깅하며, 완벽한 STAR 자소서로 만들어줍니다.</p>
    </section>

    <div class="workspace-container">

        <!-- [기능 1] AI 마이크로 체크리스트 -->
        <div class="card">
            <div class="card-header">
                🎯 1. AI 목표 분해 엔진
            </div>
            <div class="goal-input-group">
                <input type="text" id="goalInput" placeholder="이루고 싶은 큰 목표를 입력하세요. (예: 삼성전자 설비보전직 서류 합격)">
                <button class="btn-primary" onclick="generateTasks()" style="display:flex; align-items:center;">
                    분해하기 <div class="spinner" id="taskSpinner"></div>
                </button>
            </div>
            <div class="task-list" id="taskList" style="display:none;">
                <div class="task-item">
                    <div class="task-text">✅ 오늘 15분: 미쓰비시 PLC 기본 도면 1개 해석하기</div>
                    <div class="task-tag">직무역량</div>
                </div>
                <div class="task-item">
                    <div class="task-text">✅ 오늘 10분: 어제 작성한 시퀀스 회로 오답노트 복습</div>
                    <div class="task-tag">반복학습</div>
                </div>
            </div>
        </div>

        <!-- [기능 2] Vision AI 캘린더 로깅 -->
        <div class="card">
            <div class="card-header">
                📷 2. Vision AI 실습 자동 로깅
            </div>
            <p style="color:#6b7684; font-size:15px; margin-bottom:20px;">복잡하게 글을 쓸 필요 없습니다. 오늘 완성한 실습 결과물 사진을 올려주세요.</p>
            <div class="upload-area" onclick="simulateVisionUpload()">
                <div class="upload-icon">📸</div>
                <div class="upload-text">여기를 클릭하여 실습 사진 업로드 (웹캠 촬영 가능)</div>
            </div>
            <div id="visionResult">
                <div style="font-weight:bold; color:#191F28; margin-bottom:10px;">AI 시맨틱 분석 완료 (캘린더 자동 저장)</div>
                <div id="visionTags">
                    <!-- 태그가 JavaScript로 삽입됩니다. -->
                </div>
                <p style="margin-top:10px; font-size:14px; color:#4e5968;">인식된 장비: 아두이노 우노, 브레드보드, 초음파 센서, 점퍼 케이블</p>
            </div>
        </div>

        <!-- [기능 3] STAR 자소서 생성 -->
        <div class="card">
            <div class="card-header">
                ✨ 3. AI STAR 자소서 추출
            </div>
            <p style="color:#6b7684; font-size:15px; margin-bottom:20px;">캘린더에 쌓인 2학년 2학기 데이터를 바탕으로 문제해결 역량 자소서를 생성합니다.</p>
            <button class="btn-primary" onclick="generateResume()" style="display:flex; align-items:center; width: 100%; justify-content: center;">
                경험 데이터로 자소서 추출하기 <div class="spinner" id="resumeSpinner"></div>
            </button>

            <div id="resumeResult">
                <div class="resume-title">📝 문제해결 역량 에피소드 (AI 초안)</div>
                <div class="resume-content">
                    <div class="star-section"><span class="star-label">[Situation]</span> 2학년 2학기 PLC 자동제어 실습 프로젝트 중, 컨베이어 벨트 모형이 센서 오작동으로 멈추는 문제가 발생했습니다.</div>
                    <div class="star-section"><span class="star-label">[Task]</span> 저는 팀의 회로 담당으로서 30분 내에 센서 신호 누락 원인을 파악하고 회로를 수정해야 하는 과제를 맡았습니다.</div>
                    <div class="star-section"><span class="star-label">[Action]</span> 먼저 캘린더에 기록해 둔 'PLC 제어 도면 해석' 지식을 바탕으로 멀티미터를 활용해 초음파 센서와 아두이노 간의 전압 강하를 확인했습니다. 이후, 노이즈를 줄이기 위해 저항을 추가하고 케이블 라우팅을 재배치했습니다.</div>
                    <div class="star-section"><span class="star-label">[Result]</span> 그 결과 센서 인식률을 95% 이상으로 끌어올려 프로젝트를 성공적으로 마칠 수 있었으며, 이는 꾸준히 실습 스냅샷을 기록하며 트러블슈팅 과정을 복기한 덕분입니다.</div>
                </div>
            </div>
        </div>

    </div>

    <script>
        // 토스 스타일의 부드러운 UI 시뮬레이션 스크립트
        function generateTasks() {
            const input = document.getElementById('goalInput').value;
            if(!input) { alert("목표를 입력해주세요."); return; }

            const spinner = document.getElementById('taskSpinner');
            const taskList = document.getElementById('taskList');

            spinner.style.display = 'block';
            taskList.style.display = 'none';

            setTimeout(() => {
                spinner.style.display = 'none';
                taskList.style.display = 'flex';
            }, 1200); // AI 로딩 효과
        }

        function simulateVisionUpload() {
            const resultBox = document.getElementById('visionResult');
            const tagsBox = document.getElementById('visionTags');

            resultBox.style.display = 'none';

            setTimeout(() => {
                resultBox.style.display = 'block';
                tagsBox.innerHTML = `
                    <span class="tag-pill">#회로설계</span>
                    <span class="tag-pill">#아두이노</span>
                    <span class="tag-pill">#트러블슈팅</span>
                    <span class="tag-pill">#팀워크</span>
                `;
            }, 800);
        }

        function generateResume() {
            const spinner = document.getElementById('resumeSpinner');
            const resultBox = document.getElementById('resumeResult');

            spinner.style.display = 'block';
            resultBox.style.display = 'none';

            setTimeout(() => {
                spinner.style.display = 'none';
                resultBox.style.display = 'block';
            }, 1500);
        }
    </script>
</body>
</html>
