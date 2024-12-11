import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import matplotlib  # 한글 폰트 설정용

# 한글 폰트 설정
matplotlib.rc('font', family='Malgun Gothic')  # Windows 환경 (Mac에서는 'AppleGothic')

def visualize_performance(scores, labels, title, ylabel, bar_color='skyblue'):
    """
    성능 점수를 시각화하며 Gaussian 신뢰 구간을 포함합니다.
    """
    if len(scores) != len(labels):
        raise ValueError("scores와 labels의 길이가 같아야 합니다.")
    
    # Gaussian 신뢰 구간 계산
    mean = np.mean(scores)
    std = np.std(scores)
    
    if std == 0:  # 표준 편차가 0인 경우 처리
        conf_interval = (mean, mean)  # 신뢰 구간이 의미 없으므로 평균선만 표시
    else:
        conf_interval = norm.interval(0.95, loc=mean, scale=std)  # 95% 신뢰 구간

    # 막대 그래프 생성
    plt.figure(figsize=(10, 6))
    plt.bar(labels, scores, color=bar_color, edgecolor='black', alpha=0.7)
    plt.axhline(mean, color='red', linestyle='--', label=f'평균: {mean:.2f}')
    
    if std != 0:  # 신뢰 구간 시각화 (표준 편차가 0이 아닐 때만)
        plt.fill_between(
            range(len(scores)), conf_interval[0], conf_interval[1],
            color='yellow', alpha=0.2, label='95% 신뢰 구간'
        )
    
    # 제목 및 축 레이블
    plt.title(title, fontsize=18, weight='bold')
    plt.xlabel("샘플", fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    # X축 및 Y축 눈금 설정
    plt.xticks(range(len(labels)), labels, rotation=0, fontsize=12)
    plt.yticks(range(0, 101, 10))  # Y축 눈금을 0에서 100까지 10 단위로 설정
    
    # 그래프 시각적 개선
    plt.ylim(0, 100 if "신뢰도" in ylabel else max(scores) * 1.2)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()

def visualize_tts_durations(durations, labels, title, ylabel, bar_color='lightgreen'):
    """
    TTS 처리 시간의 평균, 표준 편차, 최대/최소 값을 시각화합니다.
    """
    if len(durations) != len(labels):
        raise ValueError("durations와 labels의 길이가 같아야 합니다.")
    
    # 계산
    mean = np.mean(durations)
    std = np.std(durations)
    max_time = max(durations)
    min_time = min(durations)
    
    # 막대 그래프 생성
    plt.figure(figsize=(10, 6))
    plt.bar(labels, durations, color=bar_color, edgecolor='black', alpha=0.7)
    plt.axhline(mean, color='blue', linestyle='--', label=f'평균 처리 시간: {mean:.2f}초')
    plt.fill_between(
        range(len(durations)), 
        [mean - std] * len(durations), 
        [mean + std] * len(durations),
        color='yellow', alpha=0.2, label=f'±표준 편차: {std:.2f}초'
    )
    
    # 최대/최소 값 강조
    max_index = durations.index(max_time)
    min_index = durations.index(min_time)
    plt.scatter([max_index], [max_time], color='red', label=f'최대: {max_time:.2f}초')
    plt.scatter([min_index], [min_time], color='purple', label=f'최소: {min_time:.2f}초')
    
    # 그래프에 평균, 표준 편차, 최대/최소 값 텍스트 표시
    plt.text(len(durations) - 1, mean, f'평균: {mean:.2f}초', color='blue', fontsize=12, ha='center')
    plt.text(max_index, max_time + 0.5, f'{max_time:.2f}초', color='red', fontsize=12, ha='center')
    plt.text(min_index, min_time - 0.5, f'{min_time:.2f}초', color='purple', fontsize=12, ha='center')

    # 제목 및 축 레이블
    plt.title(title, fontsize=18, weight='bold')
    plt.xlabel("샘플", fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    # X축 및 Y축 눈금 설정
    plt.xticks(range(len(labels)), labels, rotation=0, fontsize=12)
    plt.yticks(np.arange(0, max(durations) * 1.2, step=max(durations) / 10))  # 동적 눈금 설정
    
    # 그래프 시각적 개선
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()
