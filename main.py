# Part 1
from os import read


def read_csv(filename):
  """
  description --> takes in a csv file and outputs the header of data in files and the data with its elements converted to the appropriate type
  
  parameters: filename --> the csv file to unpack and extract data from

  returns: header --> the a list containing labels, data --> a nested list of data

  examples: read_csv("fruits_amount.csv") --> ["fruits","amount"], [["apples",30],["bananas",20]]
  
  """
    # Type your code below
  with open(filename,"r") as f:
    header = f.readline()
    data = []
    for i in f:
        temp = i.strip().split(",")
        temp[0] = int(temp[0])
        temp[3] = int(temp[3])
        data.append(temp)
    return header,data
    


# Part 2
def filter_gender(enrolment_by_age, sex):
    # Type your code below
    """
    description --> takes in records and a gender and returns only records under that gender

    parameters --> enrolment_by_age, a nested list which contains records , sex, the gender to identify wanted records

    return --> temp, a list which contains only the wanted records

    examples --> filter_gender([[1984,'15 yrs','MF',8710],[1996,'17 yrs','M',910]],"MF") --> [[1984,'15 yrs','MF',8710]]
    
    """
    temp = []
    for i in enrolment_by_age:
        if i[2] == sex:
            temp.append([i[0],i[1],i[3]])
    return temp      
            
  


# Part 3
def sum_by_year(enrolment):
    # Type your code below
    """
    description --> sum enrolment based of year 
    parameters --> records of enrolment data
    returns --> a nested list containing the year and the total enrolment of that year
    examples --> sum_by_year([[1984,'15 yrs',8710],[1984,'15 yrs','1010'],[1900,'15 yrs','410']]) --> [[1984,9720],[1900,410]]
    
    """
    temp = {}
    output = []
    for i in enrolment:
        if i[0] in temp:
            temp[i[0]] += i[2]
        else:
            temp[i[0]] = i[2]
    for i in temp:
        output.append([i,temp[i]])
    return output


# Part 4
def write_csv(filename, header, data):
    # Type your code below
    """
    description --> rewrite a file with headers and its data and return a number of lines written
    parameters --> filename: the file to be rewritten, header: the list of headers, data: a nested list of data with each element corresponding to the elements in header
    example --> write_csv("temp.csv",["lives","damage"],[[99,8],[1,20]]) --> 3
    """
    with open(filename, "w") as f:
        for a in header:
            if a != header[-1]:
                f.write(str(a)+",")
            else:
                f.write(str(a))
        for i in data:
            f.write("\n")
            for j in i:
                if j != i[-1]:
                    f.write(str(j)+",")
                else:
                    f.write(str(j))
    return len(data)

# TESTING
# You can write code below to call the above functions
# and test the output
#mfenrol = filter_gender(read_csv("pre-u-enrolment-by-age.csv")[1],"MF")
#enrolbyyear = sum_by_year(mfenrol)
#print(write_csv('t-e-b-y.csv',["year","t_enrol"],enrolbyyear))
#print(read_csv("pre-u-enrolment-by-age.csv")[1])

