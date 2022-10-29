import FieldTrip

c = FieldTrip.Client()
c.connect(hostname='127.0.0.1')
import pdb; pdb.set_trace()
h = c.getHeader()
print('number of channels ' + str(h.nChannels))

