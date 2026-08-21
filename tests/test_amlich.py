import unittest

from cal import amlich


class SolarToLunarTest(unittest.TestCase):

    def test_leap_month(self):
        self.assertEqual(amlich.S2L(12, 9, 2006), [20, 7, 2006, 1])
        self.assertEqual(amlich.S2L(13, 8, 2006), [20, 7, 2006, 0])
        self.assertEqual(amlich.S2L(12, 6, 2012), [23, 4, 2012, 1])
        self.assertEqual(amlich.S2L(13, 5, 2012), [23, 4, 2012, 0])

    def test_leap_month_boundary_2025(self):
        '''The day before leap month 6 of 2025 starts.'''
        self.assertEqual(amlich.S2L(24, 7, 2025), [30, 6, 2025, 0])
        self.assertEqual(amlich.S2L(25, 7, 2025), [1, 6, 2025, 1])

    def test_before_2000(self):
        '''Dates before 2000-01-01 give a negative Julian century, and so a
        negative sun longitude before normalization. Truncating towards zero
        instead of flooring there used to put these a whole month early.'''
        for (dd, mm, yy), want in [
            ((1, 1, 1900), [1, 12, 1899, 0]),
            ((1, 1, 1917), [8, 12, 1916, 0]),
            ((1, 1, 1936), [7, 12, 1935, 0]),
            ((1, 1, 1955), [8, 12, 1954, 0]),
            ((1, 1, 1974), [9, 12, 1973, 0]),
            ((1, 1, 1990), [5, 12, 1989, 0]),
            ((1, 1, 1998), [4, 12, 1997, 0]),
        ]:
            self.assertEqual(amlich.S2L(dd, mm, yy), want)

    def test_tet_before_2000(self):
        for (dd, mm, yy), lunar_year in [
            ((6, 2, 1970), 1970),
            ((15, 2, 1991), 1991),
            ((16, 2, 1999), 1999),
        ]:
            self.assertEqual(amlich.S2L(dd, mm, yy), [1, 1, lunar_year, 0])


class LunarToSolarTest(unittest.TestCase):

    def test_leap_month(self):
        self.assertEqual(amlich.L2S(20, 7, 2006, 1), [12, 9, 2006])
        self.assertEqual(amlich.L2S(20, 7, 2006, 0), [13, 8, 2006])
        self.assertEqual(amlich.L2S(23, 4, 2012, 1), [12, 6, 2012])
        self.assertEqual(amlich.L2S(23, 4, 2012, 0), [13, 5, 2012])


class RoundTripTest(unittest.TestCase):

    def test_round_trip_1800_2100(self):
        for jd in range(amlich.jdFromDate(1, 1, 1800),
                        amlich.jdFromDate(31, 12, 2100) + 1):
            dd, mm, yy = amlich.jdToDate(jd)
            lunar = amlich.S2L(dd, mm, yy)
            back = amlich.L2S(lunar[0], lunar[1], lunar[2], lunar[3])
            self.assertEqual(back, [dd, mm, yy])


if __name__ == '__main__':
    unittest.main()
