#!/bin/bash
echo "Running question1...";
python ./question1.py
echo "completed";
echo "1 json file created";
echo "neighbor-district-modified.json";

echo "Running question2...";
echo "Running time -> 5 min "
python ./question2.py
echo "completed";
echo "3 csv files created ";
echo "Cases-week.csv, Cases-Month.csv, cases-overall.csv";

