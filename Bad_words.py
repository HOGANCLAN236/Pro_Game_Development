#from profanity_check import predict_prob, predict
from better_profanity import profanity
#from sklearn.externals import joblib

# predict(["hello how are you"])

# predict_prob(["hello how are you"])

profanity.load_censor_words()
result = profanity.contains_profanity("")
print(result)