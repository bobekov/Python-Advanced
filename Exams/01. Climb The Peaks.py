from collections import deque

daily_portions = [int(x) for x in input().split(', ')]
daily_stamina = deque([int(x) for x in input().split(', ')])

day = 1
peaks = deque([('Vihren', 80), ('Kutelo', 90), ('Banski Suhodol', 100), ('Polezhan', 60), ('Kamenitza', 70)])
climb_peaks = []

while daily_portions and daily_stamina and day < 8 and peaks:
    current_portion = daily_portions.pop()
    current_stamina = daily_stamina.popleft()
    sum_provision = current_portion + current_stamina

    current_peak = peaks.popleft()
    if sum_provision >= current_peak[1]:
        climb_peaks.append(current_peak[0])
        day += 1
    else:
        peaks.appendleft(current_peak)
        day += 1

if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if climb_peaks:
    print("Conquered peaks:")
    for peak in climb_peaks:
        print(peak)