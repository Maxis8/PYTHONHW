from sort import sort,get_da,sort1
from view import get_choice,get_data
from write_read_file import read_file,write_file
from main import sort_data


def start():
    return sort_data(get_choice,read_file,write_file,sort,sort1,get_da,get_data)