from django.db import models

# 🔹 Base User
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


# 🔹 Employer Profile
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name


# 🔹 Candidate Profile
class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.TextField()

    def __str__(self):
        return self.user.name


# 🔹 Job
class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


# 🔹 Application
class Application(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('candidate', 'job')