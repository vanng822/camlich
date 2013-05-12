camlich
=======

Converter between Vietnamese calendar date and Western/Solar calendar date

[![build status](https://secure.travis-ci.org/vanng822/camlich.png)](http://travis-ci.org/vanng822/camlich)


## Functions

### lunar2solar(int lunar_day, int lunar_month, int lunar_year, int lunar_leap, int time_zone)
return [day, month, year, leap]

### solar2lunar(int dd, int mm, int yyyy, int time_zone)
return [day, month, year]
