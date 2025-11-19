#get the s]size of dataframe
import pandas as pd
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

#rename column
import pandas as pd
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
  students.rename(columns={'id':'student_id','first':'first_name','last':'last_name','age':'age_in_years'},inplace=True)
  return students  
