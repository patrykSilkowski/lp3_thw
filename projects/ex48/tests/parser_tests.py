from nose.tools import *
from ex48 import parser

default_subject = 'bear'
default_verb = 'eat'
default_object = 'honey'
default_stop_word = 'the'

default_tuple_subject = ('noun', default_subject)
default_tuple_verb = ('verb', default_verb)
default_tuple_object = ('noun', default_object)
default_tuple_stop = ('stop', default_stop_word)

default_word_list = [default_tuple_subject,
                     default_tuple_verb,
                     default_tuple_object]

no_subject_word_list = [default_tuple_verb, default_tuple_object]

some_stops_word_list = [default_tuple_stop,
                        default_tuple_subject,
                        default_tuple_stop,
                        default_tuple_verb,
                        default_tuple_stop,
                        default_tuple_object]

def test_parse_default_sentence():
  temp_sentence = parser.parse_sentence(default_word_list)
  assert_equal(temp_sentence.subject, default_subject)
  assert_equal(temp_sentence.verb, default_verb)
  assert_equal(temp_sentence.object, default_object)

def test_parse_no_subject_sentence():
  temp_sentence = parser.parse_sentence(no_subject_word_list)
  assert_equal(temp_sentence.subject, 'player')
  assert_equal(temp_sentence.verb, default_verb)
  assert_equal(temp_sentence.object, default_object)

def test_parse_some_stops_sentence():
  temp_sentence = parser.parse_sentence(some_stops_word_list)
  assert_equal(temp_sentence.subject, default_subject)
  assert_equal(temp_sentence.verb, default_verb)
  assert_equal(temp_sentence.object, default_object)

def test_parse_exception_parse_verb():
  assert_raises(parser.ParserError, parser.parse_verb,
                [default_tuple_stop, default_tuple_subject])

def test_parse_exception_parse_object():
  assert_raises(parser.ParserError, parser.parse_object,
                [default_tuple_stop, default_tuple_verb])

def test_parse_exception_parse_subject():
  assert_raises(parser.ParserError, parser.parse_subject,
                [default_tuple_stop, default_tuple_stop, default_tuple_stop])
