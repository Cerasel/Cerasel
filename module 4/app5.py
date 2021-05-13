def conversation():
    name = ''
    city = ''
    def hello():
        print("Hello John ")
    def response_hello():
        nonlocal name
        name = input("My name is ")
    def question():
        print(name,",how is the weather?")
    def response2():
        print(city, "is a very nice city.")
    def question2():
        nonlocal city
        city = input("Do you like")
    return hello, response_hello, question,question2,response2
c = conversation()
c[0]()
c[1]()
c[2]()
c[3]()
c[4]()