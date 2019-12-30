from __future__ import print_function, unicode_literals
import regex

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

import sys
import pandas as pd

import importlib

formulas = importlib.import_module('formulas')


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end


print('Forex Indicator Module: Main Menu')

while True:
    colNames = ['date', 'time', 'open', 'high', 'low', 'close', 'volume']
    currencies = ['AUD', 'CAD', 'CHF', 'EUR', 'GBP', 'JPY', 'NZD', 'USD']
    indicatorTypeDict = {"Baseline": "(None)", "Confirmation 1": "(None)", "Confirmation 2": "(None)", "Volume": "(None)", "Exit": "(None)"}
    questionMain = [
        {
            'type': 'list',
            'name': 'main',
            'message': 'Please select from the following options:',
            'choices': ['Select Currency Pair',
                        'About',
                        'Quit']
        }
    ]

    answerMain = prompt(questionMain, style=style)

    if 'Select Currency Pair' in answerMain.values():
        questionBase = [
            {
                'type': 'list',
                'name': 'base',
                'message': 'Select First Currency:',
                'choices': (i for i in currencies)
            }
        ]

        answerBase = prompt(questionBase, style=style)
        currencies.remove(answerBase['base'])
        questionCounter = [
            {
                'type': 'list',
                'name': 'counter',
                'message': 'Select Second Currency:',
                'choices': (i for i in currencies)
            }
        ]

        answerCounter = prompt(questionCounter, style=style)

        first = answerBase['base']
        second = answerCounter['counter']
        filename1 = str('data/2019-12-28/' + first + second + '1440.csv')
        filename2 = str('data/2019-12-28/' + second + first + '1440.csv')
        base, cross, df = "", "", ""
        try:
            df = pd.read_csv(filename1, names=colNames)
            print(filename1)
            base = filename1[16:19]
            cross = filename1[19:22]
        except IOError:
            try:
                df = pd.read_csv(filename2, names=colNames)  # header=none
                print(filename2)
                base = filename2[16:19]
                cross = filename2[19:22]
            except IOError:
                print("Sorry, file does not exist.")
                break
        print("The base currency is " + base)
        print("The cross currency is " + cross)
        print(df.head)
        # Calculating Average True Range
        df['max1'] = df['high'] - df['low']
        df['max2'] = abs(df['high'] - df['close'].shift(periods=1))
        df['max3'] = abs(df['low'] - df['close'].shift(periods=1))
        df['trueRange'] = df[['max1', 'max2', 'max3']].max(axis=1)
        df['ATR'] = df['trueRange'].rolling(window=14).mean()
        df['pipGain'] = df['close'] - df['close'].shift(periods=1)
        print(df.head)

        while True:
            questionType = [
                {
                    'type': 'list',
                    'name': 'indicatorType',
                    'message': 'Select Indicator Type:',
                    'choices': ["Baseline",
                                "Confirmation 1",
                                "Confirmation 2",
                                "Volume",
                                "Exit",
                                "Terminate"
                                ]
                }
            ]

            answerType = prompt(questionType, style=style)

            if "Baseline" in answerType.values():
                questionBaseline = [
                    {
                        'type': 'list',
                        'name': 'indicatorType',
                        'message': 'Select Indicator Type:',
                        'choices': ["Chaikin Money Flow",
                                    ]
                    }
                ]

                answerBaseline = prompt(questionBaseline, style=style)

                if "Chaikin Money Flow" in answerBaseline.values():
                    questionCMFPeriod = [
                        {
                            'type': 'input',
                            'name': 'quantity',
                            'message': 'Please input the desired period',
                            'validate': NumberValidator,
                            'default': '20',
                            'filter': lambda val: int(val)
                        }
                    ]
                    answerCMFPeriod = prompt(questionCMFPeriod, style=style)
                    pprint(answerCMFPeriod)
                    indicatorTypeDict['Baseline'] = str(answerBaseline) + str(
                        answerCMFPeriod.values)
                    pprint(indicatorTypeDict)
                    formulas.chaikin_money_flow(df=df, period=20)
                    print(df)
                    continue

            if "Confirmation 1" in answerType.values():
                questionConf1 = [
                    {
                        'type': 'list',
                        'name': 'confirmation1',
                        'message': 'Select Indicator Type:',
                        'choices': ["Rate Of Change",
                                    ]
                    }
                ]

                answerConf1 = prompt(questionConf1, style=style)
                if "Rate Of Change" in answerConf1.values():
                    questionROCPeriod = [
                        {
                            'type': 'input',
                            'name': 'ROCPeriod',
                            'message': 'Please input the desired period',
                            'validate': NumberValidator,
                            'default': '20',
                            'filter': lambda val: int(val)
                        }
                    ]
                    answerROCPeriod = prompt(questionROCPeriod, style=style)
                    pprint(answerROCPeriod)
                    indicatorTypeDict['Confirmation 1'] = str(answerROCPeriod) + str(
                        answerROCPeriod.values)
                    pprint(indicatorTypeDict)
                    formulas.rate_of_change(df=df, period=20)
                    print(df)
                    continue

            if "Confirmation 2" in answerType.values():
                print("todo")

            if "Volume" in answerType.values():
                print("todo")

            if "Exit" in answerType.values():
                questionExit = [
                    {
                        'type': 'list',
                        'name': 'exit',
                        'message': 'Select Indicator Type:',
                        'choices': ["Relative Vigor Index",
                                    ]
                    }
                ]
                answerExit = prompt(questionExit, style=style)
                if "Relative Vigor Index" in answerExit.values():
                    questionROCPeriod = [
                        {
                            'type': 'input',
                            'name': 'ROCPeriod',
                            'message': 'Please input the desired period',
                            'validate': NumberValidator,
                            'default': '20',
                            'filter': lambda val: int(val)
                        }
                    ]
                    answerROCPeriod = prompt(questionROCPeriod, style=style)
                    pprint(answerROCPeriod)
                    indicatorTypeDict['Exit'] = str(answerROCPeriod) + str(
                        answerROCPeriod.values)
                    pprint(indicatorTypeDict)
                    formulas.rate_of_change(df=df, period=20)
                    print(df)
                    continue
            if "Terminate" in answerType.values():
                sys.exit(1)

    if 'About' in answerMain.values():
        print("todo")

    if 'Quit' in answerMain.values():
        print("Thank you for using the Forex Indicator Module.")
        sys.exit(1)
