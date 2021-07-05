def words_to_companies(scores, words):
    """scans I-ORG word tokens to form complete company names and respective aggregated confidences
    :param scores:[float] confidence scores of each word token
    :param words:[str] word tokens

    :return aggregated confidences:[float], joined and refined company names:[str]
    """
    names = []
    confidences = []
    lastname = ""
    for i in range(len(words)):
        if (
            "##" in words[i]
            or words[i] == "-"
            or str(lastname[-1] if len(lastname) > 0 else "") == "-"
        ):
            lastname = lastname + words[i].replace("#", "")
            names[-1] = lastname
            confidences[-1] = (confidences[-1] + float(scores[i])) / 2
        else:
            names.append(words[i])
            lastname = words[i]
            confidences.append(float(scores[i]))
    return confidences, names
