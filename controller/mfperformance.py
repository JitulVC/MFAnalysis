from flask import Flask, request, jsonify, render_template, redirect
from http import HTTPStatus
import pandas as p
from json import loads, dumps

from models.mfperformance import MFPerformance

class MFPerformanceController:     
    def __mfanalyze(self,qdata):
        df = p.read_excel('Historical Returns - Mutual fund.xlsx',sheet_name='Sheet1',usecols = 'A,D,J,K,L,M,N')

        df.drop(df[df['1Y'] == '-'].index, inplace = True)
        df.drop(df[df['2Y'] == '-'].index, inplace = True)
        df.drop(df[df['5Y'] == '-'].index, inplace = True)
        df.drop(df[df['YTD'] == '-'].index, inplace = True)

        df['1Y'] = df['1Y'].astype(float)*100
        df['2Y'] = df['2Y'].astype(float)*100
        df['3Y'] = df['3Y'].astype(float)*100
        df['5Y'] = df['5Y'].astype(float)*100
        df['YTD'] = df['YTD'].astype(float)*100

        if qdata['crisilrankf'] >=0 and qdata['crisilrankt'] > 0:
            df = df.loc[(df['Crisil Rank'] > qdata['crisilrankf']) & (df['Crisil Rank'] < qdata['crisilrankt'])]
        if qdata['ytdreturnf'] >=0 and qdata['ytdreturnt'] > 0:
            df = df.loc[(df['YTD'] > qdata['ytdreturnf']) & (df['YTD'] < qdata['ytdreturnt'])]
        if qdata['oneyreturnf'] >=0 and qdata['oneyreturnt'] > 0:
            df = df.loc[(df['1Y'] > qdata['oneyreturnf']) & (df['1Y'] < qdata['oneyreturnt'])]
        if qdata['twoyreturnf'] >=0 and qdata['twoyreturnt'] > 0:
            df = df.loc[(df['2Y'] > qdata['twoyreturnf']) & (df['2Y'] < qdata['twoyreturnt'])]
        if qdata['threeyreturnf'] >=0 and qdata['threeyreturnt'] > 0:
            df = df.loc[(df['3Y'] > qdata['threeyreturnf']) & (df['3Y'] < qdata['threeyreturnt'])]
        if qdata['fiveyreturnf'] >=0 and qdata['fiveyreturnt'] > 0:
            df = df.loc[(df['5Y'] > qdata['fiveyreturnf']) & (df['5Y'] < qdata['fiveyreturnt'])]

        dj = df.to_json(orient="records")
        dj = loads(dj)
        return dj

    def mfperformance(self, qdata):
        data = self.__mfanalyze(qdata)
        return render_template('mfanalysis.html', mfperformance=data,qstr=qdata)

