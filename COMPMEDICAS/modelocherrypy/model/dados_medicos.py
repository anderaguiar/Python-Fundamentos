
#class
class DadosMedicos:
    autor = None
    filename = None
    date = None
    title = None
    patient = None
    keywords = None
    especiality = None
    diagnostic = None

    # constructor
    def __init__(self, autor, filename, date, title, patient, keywords, especiality, diagnostic):
        self.autor = autor
        self.filename = filename
        self.date = date
        self.title = title
        self.patient = patient
        self.keywords = keywords
        self.especiality = especiality
        self.diagnostic = diagnostic

    #set
    def setAutor(self, autor):
        self.autor = autor
    def setFilename(self, filename):
        self.filename = filename
    def setDate(self,date):
        self.date = date
    def setTitle(self, title):
        self.title = title
    def setPatient(self, patient):
        self.patient = patient
    def setKeywords(self, keywords):
        self.keywords = keywords
    def setEspeciality(self, especiality):
        self.especiality = especiality
    def setDiagnostic(self, diagnostic):
        self.diagnostic = diagnostic

    # get
    def getAutor(self):
        return self.autor
    def getFilename(self):
        return self.filename
    def getDate(self):
        return self.date
    def getTitle(self):
        return self.title
    def getPatient(self):
        return self.patient
    def getKeywords(self):
        return self.keywords
    def getEspeciality(self):
        return self.especiality
    def getDiagnostic(self):
        return self.diagnostic