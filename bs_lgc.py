import os
import pandas as pd

#------------------ Get text from the given file for the given co-ordinates of diagonal of rectangle
def get_text(x0,y0,x2,y2,fname):
    fpath = os.path.join('csvs',fname)
    df = pd.DataFrame()
    try:
        if os.path.exists(fpath):
            df = pd.read_csv(fpath)
            words_of_text= []
            for i in range(0, len(df)):
                if (int(x0) <= df.loc[i,'x0'] <= int(x2)  or int(x0) <= df.loc[i,'x2'] <= int(x2) ) and (int(y0) <= df.loc[i,'y0'] <= int(y2)  or int(y0) <= df.loc[i,'y2'] <= int(y2)):
                    words_of_text.append(str(df.loc[i,'Text']))
            result = ' '.join(words_of_text)
            return result
        else:
            raise FileNotFoundError('File does not exists at given path')

    except FileNotFoundError:
        return 'File does not exists at given path'
    except:
        return 'Some error occured'

