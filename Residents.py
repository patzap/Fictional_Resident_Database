class Residents:

    def __init__(self, res_id, res_name, date_occup, care_type, style_suite):

        self.res_id = res_id
        self.res_name = res_name
        self.date_occup = date_occup
        self.care_type = care_type
        self.style_suite = style_suite
       

    def __repr__(self):
        return "Residents('{}', '{}','{}', '{}', '{}')".format(self.res_id, self.res_name, self.date_occup, self.care_type, self.style_suite)