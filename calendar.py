class MeeteingCalendar:
	'''Simple implementation of a meeting calendar'''
	def __init__(self, employment, *, boundary='8:00-20:00', duration=60):
		self._activity = boundary
		self._boundary = self._time2mins([boundary])
		self._duration = int(duration)
		self._busy = self._time2mins(employment)
		self._free = self._free_time()

	def _time2mins(self, time):
		'''['10:00-11:30', ..., '17:45-20:00'] -> [[600, 690], ..., [1065, 1200]]'''
		mins = []
		for t in time:
			start, end = t.split('-')
			h_start, m_start = start.split(':')
			h_end, m_end = end.split(':')
			mins.append([
				60 * int(h_start) + int(m_start), 
				60 * int(h_end) + int(m_end)
			])

		return mins

	def _mins2time(self, mins):
		'''[[600, 690], ..., [1065, 1200]] -> ['10:00-11:30', ..., '17:45-20:00'] '''
		time = []
		for m in mins:
			start, end = m
			h_start, m_start = start // 60, start % 60
			h_end, m_end = end // 60, end % 60

			m_start = '00' if m_start == 0 else m_start
			m_end = '00' if m_end == 0 else m_end

			time.append(f'{h_start}:{m_start}-{h_end}:{m_end}')

		return time

	def _free_time(self):
		'''Free time in minutes according to busy time'''
		free = []
		if self._busy[0][0] - self._boundary[0][0] > self._duration:
			free.append([self._boundary[0][0], self._busy[0][0]])

		for i in range(len(self._busy) - 1):
			start, end = self._busy[i]
			next_start, next_end = self._busy[i+1]
			if next_start - end > self._duration:
				free.append([end, next_start])

		if self._boundary[0][-1] - self._busy[-1][1] > self._duration:
			free.append([self._busy[-1][1], self._boundary[0][-1]])

		return free

	def get_free_mins(self):
		'''Free time in minutes'''
		return self._free

	def get_free_time(self):
		'''Free time intervals'''
		return self._mins2time(self._free)

	def get_busy_mins(self):
		'''Busy time in minutes'''
		return self._busy

	def get_busy_time(self):
		'''Busy time intervals'''
		return self._mins2time(self._busy)

	def posseble_meeting(self, calendar):
		'''Possible time to meet with the person'''
		possibilities = []
		duration = max(self._duration, calendar._duration)
		for free1, free2 in zip(self._free, calendar._free):
			set1 = set(range(free1[0], free1[1] + 1, duration))
			set2 = set(range(free2[0], free2[1] + 1, duration))
			intersection = set1 & set2
			if intersection:
				possibilities.append([min(intersection), max(intersection)])

		return self._mins2time(possibilities)

	def __repr__(self):
		boundary = f'Activity time: {self._activity}\n'
		duration = f'Required meeting time: {self._duration}\n'
		busy_time = f'Busy time: {self.get_busy_time()}\n'
		free_time = f'Free time: {self.get_free_time()}\n'
		return boundary + duration + busy_time + free_time


if __name__ == '__main__':
	calendar1 = MeeteingCalendar(['10:00-12:10', '13:00-14:00', '16:40-19:10'], duration=40)
	calendar2 = MeeteingCalendar(['9:45-10:00', '13:00-14:20', '15:45-18:20'], duration=60)
	meetings = calendar1.posseble_meeting(calendar2)

	print(calendar1)
	print(calendar2)
	print(f'Possible meeting times: {meetings}')
