from docassemble.base.util import DAList, DAObject

__all__ = ['Agency', 'CaseList', 'Case', 'ChargeList', 'Charge']

class Agency(DAObject):
    def init(self, *pargs, **kwargs):
        self.complete_attribute = 'agency_complete'
        super(Agency, self).init(*pargs, **kwargs)
    
    @property
    def agency_complete(self):
        self.name

    def __unicode__(self):
        return self.name
        
class CaseList(DAList):
    def init(self, *pargs, **kwargs):
        self.object_type = Case
        self.complete_attribute = 'case_complete'
        super(CaseList, self).init(*pargs, **kwargs)

class Case(DAObject):
    def init(self, *pargs, **kwargs):
      if 'charges' not in kwargs:
          self.initializeAttribute('charges', ChargeList)
      super(Case, self).init(*pargs, **kwargs)
        
    @property
    def case_complete(self):
        self.docket_number
        self.otn
        self.dc
        self.arrest_date
        self.affiant
        self.judge_address
        self.judge_name

    def __unicode__(self):
        return self.docket_number
      
class ChargeList(DAList):
    def init(self, *pargs, **kwargs):
        self.object_type = Charge
        self.complete_attribute = "charge_complete"
        super(ChargeList, self).init(*pargs, **kwargs)
        
class Charge(DAObject):
    @property
    def charge_complete(self):
        self.section_number
        self.offense_name
        self.offense_grade
        self.disposition
        
    def __unicode__(self):
        return self.offense_name