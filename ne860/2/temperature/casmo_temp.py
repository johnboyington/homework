import re


class Casmo_Input(object):
    def __init__(self, name, ID, tfu, tco, p):
        self.tfu = tfu
        self.tco = tco
        self.p = p
        self.name = name
        self.write_input()
    
    def write_input(self):
        s = "TTL *Four Factors\n"
        s += "TFU={:3} TCO={:3} TMO=300   		*Statepoint parameters\n".format(self.tfu, self.tco)
        s += "FUE 1 10.0/4.0            		*Fuel density/enrichment\n"
        s += "PIC {:5.4},{:5.4},{:5.4f},0.710766/'fuel','Air','CAN','BOX'\n".format(self.p, self.p + .0084, self.p + .0654)
        s += "STA                      		*Start execution\n"
        s += "END                       		*End of input\n"
        
        with open('{}.inp'.format(self.name), 'w+') as F:
            F.write(s)

class Casmo_Output(object):

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

        # relevent parameters
        self.phi1 = None
        self.phi2 = None
        self.nufiss1 = None
        self.nufiss2 = None
        self.abs1 = None
        self.abs2 = None

        self.eta = None
        self.f = 1
        self.p = None
        self.epsilon = None
        self.k_inf = None

        # grab the above values
        self.grab_values()

        # calculate the four factors
        try:
            self.four_factors()
        except:
            pass

    def grab_values(self):
        with open(self.name, 'r') as F:
            lines = F.readlines()
        value = r'\d.\d\d\d\dE[+-]\d\d'
        value = re.compile(value)
        for line in lines:
            # grab phis
            if 'FLUX  . . . . . . .' in line:
                values = value.findall(line)
                self.phi1, self.phi2 = float(values[0]), float(values[1])

            # grab nufiss values
            if 'NUFISS1 , NUFISS2' in line:
                values = value.findall(line)
                self.nufiss1, self.nufiss2 = float(values[0]), float(values[1])

            # grab abs values
            if 'ABS1    , ABS2' in line:
                values = value.findall(line)
                self.abs1, self.abs2 = float(values[0]), float(values[1])

    def four_factors(self):
        # calculate eta
        self.eta = (self.nufiss2 * self.phi2) / (self.abs2 * self.phi2)

        # f is assumed to be 1
        self.f = 1

        # calculate p
        self.p = (self.abs2 * self.phi2) / (self.abs2 * self.phi2 + self.abs1 * self.phi1)

        # calculate epsilon
        self.epsilon = (self.nufiss1 * self.phi1 + self.nufiss2 * self.phi2) / (self.nufiss2 * self.phi2)

        # calculate k infinity
        self.k_inf = self.eta * self.f * self.p * self.epsilon


if __name__ == '__main__':
    pass