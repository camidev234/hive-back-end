from users.models.profile import Profile


class ProfileService():
    def save_profile(self, user):
        profile = Profile()
        profile.user = user
        profile.save()
        
        print(profile.id)
        print(profile.user_id)
        
        return True