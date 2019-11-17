from openpyxl import load_workbook, Workbook
from openpyxl.styles import Color, PatternFill as Pf, Font, Border
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, FormulaRule

darkRedFill = Pf(start_color='FF3333', end_color='FF3333', fill_type='solid')
redFill = Pf(start_color='FF0000', end_color='FF0000', fill_type='solid')
pinkFill = Pf(start_color='FFAFAF', end_color='FFAFAF', fill_type='solid')
ltGreenFill = Pf(start_color='72FF76', end_color='72FF76', fill_type='solid')
greenFill = Pf(start_color='2CD731', end_color='2CD731', fill_type='solid')
darkGreenFill = Pf(start_color='23A627', end_color='23A627', fill_type='solid')

wb = load_workbook(r'C:\GithubProjects\Indicators\output\test5.xlsx')
ws = wb.active

maxRow = ws.max_row

tpMult = 1
slMult = 1

cellList = []
for sheet in wb.worksheets:
    roc = sheet['G2'].value
    sign = (roc / abs(roc))
    direction = 0
    if sign > 0:
        direction = 'long'
    else:
        direction = 'short'
    takeProfit = sheet['C2'].value + (sheet['D2'].value * (roc / abs(roc)))
    stopLoss = sheet['C2'].value - (sheet['D2'].value * (roc / abs(roc)))
    tpTarget = takeProfit * tpMult
    slTarget = stopLoss * slMult
    sheet['H2'].value = 'Entering ' + direction + ' at '
    sheet['H3'].value = str(sheet['C2'].value)
    sheet['H5'].value = 'Take Profit at:'
    sheet['H6'].value = str(tpTarget)
    sheet['H8'].value = 'Stop Loss at'
    sheet['H9'].value = str(slTarget)
    sheet['I1'].value = 'DistanceToTP'
    sheet['J1'].value = 'DistanceToSL'
    for x in range(2, maxRow):
        iRange, jRange, cRange = 'I' + str(x), 'J' + str(x), 'C' + str(x)
        cRangePrev = 'C' + str(x - 1)
        close = sheet[cRange].value
        if close is None:
            continue
        sheet[iRange].value = float(close) - tpTarget
        sheet[jRange].value = float(close) - slTarget
    iMax, jMax = 'I' + str(maxRow), 'J' + str(maxRow)
    sheet.conditional_formatting.add('I2:' + str(iMax),
                                     CellIsRule(operator='between',
                                                formula=[('(H$6 - H$3) * 2'),
                                                         ('(H$6 - H$3) * 1')],
                                                stopIfTrue=True,
                                                fill=darkGreenFill))
    sheet.conditional_formatting.add('I2:' + str(iMax),
                                     CellIsRule(operator='between',
                                                formula=[('(H$6 - H$3) * 1'),
                                                         ('(H$6 - H$3) * .5')],
                                                stopIfTrue=True,
                                                fill=greenFill))
    sheet.conditional_formatting.add('I2:' + str(iMax),
                                     CellIsRule(operator='between',
                                                formula=[('(H$9 - H$3) * .5'),
                                                         ('(H$9 - H$3) * .01')],
                                                stopIfTrue=True,
                                                fill=ltGreenFill))
    sheet.conditional_formatting.add('J2:' + str(jMax),
                                     CellIsRule(operator='between',
                                                formula=[('(H$9 - H$3) * 1'),
                                                         ('(H$9 - H$3) * .7')],
                                                stopIfTrue=True,
                                                fill=darkRedFill))
    sheet.conditional_formatting.add('J2:' + str(jMax),
                                     CellIsRule(operator='between',
                                                formula=[('(H$9 - H$3) * .7'),
                                                         ('(H$9 - H$3) * .4')],
                                                stopIfTrue=True,
                                                fill=redFill))
    sheet.conditional_formatting.add('J2:' + str(jMax),
                                     CellIsRule(operator='between',
                                                formula=[('(H$9 - H$3) * .4'),
                                                         ('(H$9 - H$3) * '
                                                          '.01')],
                                                stopIfTrue=True,
                                                fill=pinkFill))


wb.save(r'C:\GithubProjects\Indicators\output\xlsxOutput.xlsx')
