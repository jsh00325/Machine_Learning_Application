import random as rd;

SIMULATION_TIME = 100000

changeCount = 0
unchangeCount = 0

for _ in range(SIMULATION_TIME) :
	# 차가 있는 문의 번호
	carPosition = rd.randint(1, 3)

	# 첫번째로 선택할 문의 번호
	firstChoice = rd.randint(1, 3)

	# 남은 문 중에서 염소가 있는 방의 문 열기
	openDoor = rd.choice([x for x in range(1, 4) if x != firstChoice and x != carPosition])

	# 선택을 바꿨을 때
	if carPosition == [x for x in range(1, 4) if x != firstChoice and x != openDoor][0] :
		changeCount += 1

	# 선택을 유지했을 때
	if carPosition == firstChoice :
		unchangeCount += 1

print('===== {:,}번의 실행 결과 ====='.format(SIMULATION_TIME))
print('안바꿔서 맞춘 경우 : {:,}번 ({:.2f}%)'.format(changeCount, changeCount / SIMULATION_TIME * 100))
print('  바꿔서 맞춘 경우 : {:,}번 ({:.2f}%)'.format(unchangeCount, unchangeCount / SIMULATION_TIME * 100))