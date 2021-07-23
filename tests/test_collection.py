#!/usr/bin/env python
import inspect
import os
import unittest
from pathlib import Path
from shutil import copy2
from sqlite3 import Row

from discodos.config import Config
from discodos.models import Collection


class TestCollection(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        name = inspect.currentframe().f_code.co_name
        self.clname = self.__name__  # just handy a shortcut, used in test output
        print("\n{} - {} - BEGIN".format(self.clname, name))
        #log.handlers[0].setLevel("INFO")  # handler 0 is the console handler
        #log.handlers[0].setLevel("DEBUG")  # handler 0 is the console handler
        self.conf = Config()  # doesn't get path of test-db, so...
        discodos_tests = Path(os.path.dirname(os.path.abspath(__file__)))
        empty_db_path = discodos_tests / 'fixtures' / 'discobase_empty.db'
        self.db_path = discodos_tests / 'discobase.db'
        print('Database: {}'.format(copy2(empty_db_path, self.db_path)))
        print("{} - {} - END\n".format(self.clname, name))

    def debug_db(self, db_return):
        #print(db_return.keys())
        print()
        if isinstance(db_return, list):
            print('db_return is a list')
            for i in db_return:
                stringed = ''
                for j in i:
                    stringed+='{}, '.format(j)
                print(stringed)
                print()
        elif isinstance(db_return, Row):
            print('db_return is a Row')
            stringed = ''
            for i in db_return:
                stringed+='{}, '.format(i)
            print(stringed)
            print()
        else:
            print('unknown datatype, cannot debug')
        return True

    def test_get_all_db_releases(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        # instantiate the Collection model class
        self.collection = Collection(False, self.db_path)
        db_return = self.collection.get_all_db_releases()
        #self.debug_db(db_return)
        self.assertIsNotNone(db_return)
        self.assertEqual(len(db_return), 4)
        self.assertEqual(db_return[2]['discogs_id'], 123456)
        self.assertEqual(db_return[2]['discogs_title'], 'Material Love')
        #self.assertEqual(db_return[2]['import_timestamp'], '2020-01-25 22:33:35')
        self.assertEqual(db_return[2]['d_artist'], 'Märtini Brös.')
        #self.assertEqual(db_return[2]['in_d_collection'], 1)
        self.assertEqual(db_return[3]['discogs_id'], 8620643)
        self.assertEqual(db_return[3]['discogs_title'], 'The Crane')
        #self.assertEqual(db_return[3]['import_timestamp'], '2020-01-30 10:06:26')
        self.assertEqual(db_return[3]['d_artist'], 'Source Direct')
        #self.assertEqual(db_return[3]['in_d_collection'], 1)
        print("{} - {} - END".format(self.clname, name))

    def test_search_release_id(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        # instantiate the Collection model class
        self.collection = Collection(False, self.db_path)
        db_return = self.collection.search_release_id('123456')
        self.assertIsNotNone(db_return)
        self.assertEqual(len(db_return), 10)  # should be 10 columns
        self.assertEqual(db_return['discogs_id'], 123456)
        self.assertEqual(db_return['d_artist'], 'Märtini Brös.')
        self.assertEqual(db_return['discogs_title'], 'Material Love')
        print("{} - {} - END".format(self.clname, name))

    def test_search_release_offline_number(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        db_return = self.collection.search_release_offline('123456')
        self.assertIsNotNone(db_return)
        self.assertEqual(len(db_return), 10)  # should be 10 columns
        self.assertEqual(db_return['discogs_id'], 123456)
        self.assertEqual(db_return['d_artist'], 'Märtini Brös.')
        self.assertEqual(db_return['discogs_title'], 'Material Love')
        print("{} - {} - END".format(self.clname, name))

    def test_search_release_offline_number_error(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        db_return = self.collection.search_release_offline('999999')
        self.assertIsNone(db_return)
        print("{} - {} - END".format(self.clname, name))

    def test_search_release_offline_text(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        db_return = self.collection.search_release_offline('Märtini')  # artist or title
        self.assertIsNotNone(db_return)
        self.assertEqual(len(db_return), 1)  # should be a list with 1 Row
        self.assertEqual(db_return[0]['discogs_id'], 123456)
        self.assertEqual(db_return[0]['d_artist'], 'Märtini Brös.')
        self.assertEqual(db_return[0]['discogs_title'], 'Material Love')
        print("{} - {} - END".format(self.clname, name))

    def test_search_release_offline_text_multiple(self):
        print("\nTestMix.search_release_offline_text_multiple: BEGIN")
        self.collection = Collection(False, self.db_path)
        db_return = self.collection.search_release_offline('Amon')  # artist or title
        self.assertIsNotNone(db_return)
        self.assertEqual(len(db_return), 2)  # should be a list with 2 Rows
        self.assertEqual(db_return[0]['discogs_id'], 69092)
        self.assertEqual(db_return[0]['d_artist'], 'Amon Tobin')
        self.assertEqual(db_return[0]['discogs_title'], 'Out From Out Where')
        self.assertEqual(db_return[1]['discogs_id'], 919698)
        self.assertEqual(db_return[1]['d_artist'], 'Amon Tobin')
        self.assertEqual(db_return[1]['discogs_title'], 'Foley Room')
        print("TestMix.search_release_offline_text_multiple: DONE\n")

    def test_search_release_offline_text_error(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        db_return = self.collection.search_release_offline('XXX')  # artist or title
        self.assertIsNone(db_return)  # returns None if nothing found
        #self.assertEqual(db_return, [])  # FIXME should this better be empty list?
        print("{} - {} - END".format(self.clname, name))

    def test_get_tracks_by_bpm(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        db_return = self.collection.get_tracks_by_bpm(125, 6)
        self.assertIsNotNone(db_return)
        self.assertEqual(len(db_return), 3)  # should be a list with 3 Rows
        self.assertEqual(db_return[0]['d_artist'], 'Source Direct')
        self.assertEqual(db_return[0]['d_track_no'], 'AA')
        self.assertEqual(db_return[0]['chosen_bpm'], 120)
        self.assertEqual(db_return[1]['d_artist'], 'Märtini Brös.')
        self.assertEqual(db_return[1]['d_track_no'], 'A1')
        self.assertEqual(db_return[1]['chosen_bpm'], 125)
        self.assertEqual(db_return[2]['d_artist'], 'Märtini Brös.')
        self.assertEqual(db_return[2]['d_track_no'], 'B2')
        self.assertEqual(db_return[2]['chosen_bpm'], 130)
        print("{} - {} - END".format(self.clname, name))

    def test_get_tracks_by_key(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        db_return = self.collection.get_tracks_by_key("Am")
        self.assertIsNotNone(db_return)
        self.assertEqual(len(db_return), 2)  # should be a list with 2 Rows
        self.assertEqual(db_return[0]['d_artist'], 'Source Direct')
        self.assertEqual(db_return[0]['d_track_no'], 'AA')
        self.assertEqual(db_return[0]['chosen_bpm'], 120)
        self.assertEqual(db_return[1]['d_artist'], 'Märtini Brös.')
        self.assertEqual(db_return[1]['d_track_no'], 'A1')
        self.assertEqual(db_return[1]['chosen_bpm'], 125)
        print("{} - {} - END".format(self.clname, name))

    def test_search_release_online_text_multiple(self):
        print("\nTestMix.search_release_online_text_multiple: BEGIN")
        self.collection = Collection(False, self.db_path)
        if self.collection.discogs_connect(self.conf.discogs_token,
                                           self.conf.discogs_appid):
            print('We are ONLINE')
            d_return = self.collection.search_release_online('Amon Tobin')  # artist or title
            self.assertGreater(len(d_return), 770)  # list with more than 770 Release objects
            self.assertEqual(d_return.pages, 17)  # _currently_ 17 pages
            self.assertEqual(d_return.per_page, 50)  # 50 per_page
            self.assertEqual(d_return[0].id, 3618346)
            self.assertEqual(d_return[0].artists[0].name, 'Amon Tobin')
            self.assertEqual(d_return[0].title, 'Amon Tobin')  # yes, really!
            self.assertEqual(d_return[1].id, 3620565)
            self.assertEqual(d_return[1].artists[0].name, 'Amon Tobin')
            self.assertEqual(d_return[1].title, 'Amon Tobin')  # yes, really!
            self.assertEqual(d_return[1].tracklist[0].title, 'ISAM Live')
        else:
            print('We are OFFLINE, testing if we properly fail!')
            db_return = self.collection.search_release_online('Amon Tobin')  # artist or title
            self.assertFalse(db_return)
        print("TestMix.search_release_online_text_multiple: DONE\n")

    def test_search_release_online_number(self):
        print("\nTestMix.search_release_online_number: BEGIN")
        self.collection = Collection(False, self.db_path)
        if self.collection.discogs_connect(self.conf.discogs_token,
                                           self.conf.discogs_appid):
            print('We are ONLINE')
            d_return = self.collection.search_release_online('69092')
            #print(dir(d_return))
            self.assertEqual(len(d_return), 1)  # should be single release in a list!
            self.assertEqual(int(d_return[0].id), 69092)  # we get it as a string!
            self.assertEqual(d_return[0].artists[0].name, 'Amon Tobin')
            self.assertEqual(d_return[0].title, 'Out From Out Where')
        else:
            print('We are OFFLINE, testing if we properly fail!')
            d_return = self.collection.search_release_online('69092')
            self.assertFalse(d_return)  # FIXME returns list because d.release not throwing error
        print("TestMix.search_release_online_number: DONE\n")

    def test_search_release_track_offline_artist(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        dbr = self.collection.search_release_track_offline(
            artist='Märtini', release='', track='')
        #self.debug_db(dbr)
        self.assertIsNotNone(dbr)
        self.assertEqual(len(dbr), 3)  # should be a list with 3 Rows
        self.assertEqual(dbr[2]['discogs_id'], 123456)
        self.assertEqual(dbr[0]['d_artist'], 'Märtini Brös.')
        self.assertEqual(dbr[1]['discogs_title'], 'Material Love')
        print("{} - {} - END".format(self.clname, name))

    def test_search_release_track_offline_nothing(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        dbr = self.collection.search_release_track_offline(
            artist='', release='', track='')
        #self.debug_db(dbr)
        self.assertIsNotNone(dbr)
        self.assertEqual(len(dbr), 0)  # should be a list with 0 Rows
        print("{} - {} - END".format(self.clname, name))

    def test_search_release_track_offline_artist_without_tracks(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        dbr = self.collection.search_release_track_offline(
            artist='Amon', release='', track='')
        #self.debug_db(dbr)
        self.assertIsNotNone(dbr)
        self.assertEqual(len(dbr), 2)  # should be a list with 2 Rows
        self.assertEqual(dbr[0]['d_artist'], 'Amon Tobin')
        self.assertEqual(dbr[0]['discogs_title'], 'Foley Room')
        self.assertEqual(dbr[0]['d_artist'], 'Amon Tobin')
        self.assertEqual(dbr[1]['discogs_title'], 'Out From Out Where')
        print("{} - {} - END".format(self.clname, name))

    def test_search_release_track_offline_track(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        dbr = self.collection.search_release_track_offline(
            artist='', release='', track='Hedup!')
        #self.debug_db(dbr)
        self.assertIsNotNone(dbr)
        self.assertEqual(len(dbr), 1)  # should be a list with 1 Rows
        self.assertEqual(dbr[0]['d_artist'], 'Märtini Brös.')
        self.assertEqual(dbr[0]['discogs_title'], 'Material Love')
        self.assertEqual(dbr[0]['d_track_name'], 'Hedup!')
        print("{} - {} - END".format(self.clname, name))

    def test_search_release_track_offline_release(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        dbr = self.collection.search_release_track_offline(
            artist='', release='material', track='')
        #self.debug_db(dbr)
        self.assertIsNotNone(dbr)
        self.assertEqual(len(dbr), 3)  # it's one release but finds all track entries!
        self.assertEqual(dbr[0]['d_artist'], 'Märtini Brös.')
        self.assertEqual(dbr[1]['d_track_name'], 'Material Love')
        self.assertEqual(dbr[2]['discogs_title'], 'Material Love')
        print("{} - {} - END".format(self.clname, name))

    def test_search_release_track_offline_artist_release_track(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        dbr = self.collection.search_release_track_offline(
            artist='Märtini', release='material', track='cab')
        #self.debug_db(dbr)
        self.assertIsNotNone(dbr)
        self.assertEqual(len(dbr), 1)  # one track
        self.assertEqual(dbr[0]['d_artist'], 'Märtini Brös.')
        self.assertEqual(dbr[0]['d_track_name'], 'Material Love (Cab Drivers Remix)')
        self.assertEqual(dbr[0]['discogs_title'], 'Material Love')
        print("{} - {} - END".format(self.clname, name))

    def test_track_report_snippet(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        db_return = self.collection.track_report_snippet(4, 133)
        self.assertEqual(len(db_return), 3)  # a snippet is always 3 tracks
        # track 3
        self.assertEqual(db_return[0]["track_pos"], 3)
        self.assertEqual(db_return[0]["discogs_title"], "Material Love")
        self.assertEqual(db_return[0]["d_track_no"], "B1")
        self.assertEqual(db_return[0]["trans_rating"], "")
        self.assertEqual(db_return[0]["key"], None)
        self.assertEqual(db_return[0]["bpm"], 140)
        self.assertEqual(db_return[0]["a_key"], None)
        self.assertEqual(db_return[0]["a_bpm"], None)
        # track 4
        self.assertEqual(db_return[1]["track_pos"], 4)
        self.assertEqual(db_return[1]["discogs_title"], "The Crane")
        self.assertEqual(db_return[1]["d_track_no"], "AA")
        self.assertEqual(db_return[1]["trans_rating"], "")
        self.assertEqual(db_return[1]["key"], "Am")
        self.assertEqual(db_return[1]["bpm"], 120)
        self.assertEqual(db_return[1]["a_key"], None)
        self.assertEqual(db_return[1]["a_bpm"], None)
        # track 5
        self.assertEqual(db_return[2]["track_pos"], 5)
        print("{} - {} - END".format(self.clname, name))

    def test_track_report_occurences(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        db_return = self.collection.track_report_occurences(123456, 'B2')
        self.assertEqual(len(db_return), 11)  # track was used 11 times
        # check some occurences
        self.assertEqual(db_return[0]["mix_id"], 125)  # first occurence
        self.assertEqual(db_return[0]["track_pos"], 2)  # used at pos 2
        self.assertEqual(
            db_return[0]["name"],
            'test 125 last_tr, tr_of_one_mix, one_mix')
        self.assertEqual(db_return[7]["mix_id"], 132)  # 8th occurence
        self.assertEqual(db_return[7]["track_pos"], 2)  # used at pos 2
        self.assertEqual(db_return[10]["mix_id"], 135)  # 11th occurence
        self.assertEqual(db_return[10]["track_pos"], 2)  # used at pos 2
        print("{} - {} - END".format(self.clname, name))

    def test_stats_match_method_release(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        db_return = self.collection.stats_match_method_release()
        #self.debug_db(db_return)
        self.assertEqual(len(db_return), 3)  # should be a list with 4 Rows
        self.assertEqual(db_return[0]['m_match_method'], None)
        self.assertEqual(db_return[1]['m_match_method'], 'CatNo (exact)')
        self.assertEqual(db_return[2]['m_match_method'], "Discogs URL")
        print("{} - {} - END".format(self.clname, name))

    def test_d_get_first_catno(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.collection = Collection(False, self.db_path)
        if self.collection.discogs_connect(self.conf.discogs_token,
                                           self.conf.discogs_appid):
            print('We are ONLINE')
            # we need to fetch a release by id first - let's also check it
            d_return = self.collection.search_release_online('69092')
            self.assertEqual(len(d_return), 1)  # should be single release in a list!
            self.assertEqual(int(d_return[0].id), 69092)  # we get it as a string!
            self.assertEqual(d_return[0].artists[0].name, 'Amon Tobin')
            self.assertEqual(d_return[0].title, 'Out From Out Where')
            #print(d_return[0].labels)
            #for item in d_return[0].labels:
                #print(dir(item.data))
                #print(item.data.keys())
            d_return_catno = self.collection.d_get_first_catno(d_return[0].labels)
            self.assertEqual(d_return_catno, 'ZEN 70')
        else:
            print('We are OFFLINE, testing if we properly fail!')
            d_return = self.collection.search_release_online('69092')
            self.assertFalse(d_return)
            # if release can't be fetched online it does not make sense to ask
            # d_get_first_catno() to retrieve it. This should be handled elsewhere
        print("{} - {} - END".format(self.clname, name))

    @classmethod
    def tearDownClass(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        os.remove(self.db_path)
        print("{} - {} - END\n".format(self.clname, name))


if __name__ == '__main__':
    loader = unittest.TestLoader()
    ln = lambda f: getattr(TestCollection, f).im_func.func_code.co_firstlineno
    lncmp = lambda _, a, b: cmp(ln(a), ln(b))
    loader.sortTestMethodsUsing = lncmp
    unittest.main(testLoader=loader, verbosity=2)
