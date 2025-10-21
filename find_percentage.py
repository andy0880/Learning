#Find percentage
def calculate_percentage(percent, whole):
    return (percent / 100) * whole

while True:
    try:
        percent = float(input('Enter the percent value (e.g., 25 for 25%): '))
        whole = float(input('Enter the whole value: '))
        break # exit if the inputs are valid
    except:
        print('Just numbers, please!')
        
print(percent, 'percent of', whole, 'is', calculate_percentage(percent, whole))
