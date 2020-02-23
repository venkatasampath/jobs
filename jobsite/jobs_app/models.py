from django.db.models import(
    Model,
    TextField,
    CharField,
    ForeignKey,
FileField,
)


# Create your models here.
class JobListing(Model):
    jobid = CharField(max_length=50, unique=True,)
    title = TextField(null=True, blank=False)
    description = TextField(null=True, blank=True)
    def __str__(self):
        return str(self.title)

class SkillSetTrainingModules(Model):
    skillid = CharField(max_length=50, unique=True, )
    technology = TextField(null=True, blank=False)
    description = TextField(null=True, blank=True)
    courseDuration = TextField(null=True, blank=True)
    price = TextField(null=True, blank=True)
    def __str__(self):
        return str(self.technology)



class CandidatesProfile(Model):
    specializationinProfession = TextField(null=True, blank=True)
    description = TextField(null=True, blank=True)
    experience = TextField(null=True, blank=True)
    resume = FileField(upload_to='resume', default='0')
    title = ForeignKey(JobListing, on_delete=Model.CASCADE, null=True, related_name='job',)
    technology = ForeignKey(SkillSetTrainingModules, on_delete=Model.CASCADE, null=True, related_name='skillset',)


    # Create your models here.





