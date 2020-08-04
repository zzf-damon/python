# coding=utf-8
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models
import json

try:
    cred = credential.Credential("AKIDUkwvgImz0lHY0DFrRr5btCH6g16udu50", "yAQRCnBLFs2ye4LsCGDBwQeiaCXcgWDq")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "nlp.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

    req = models.SensitiveWordsRecognitionRequest()
    str = """
    昆明警方抓获毒贩5人，缴获海洛因5吨
    """
    str.encode("utf-8")
    params = {"Text": str}
    req.from_json_string(json.dumps(params))

    resp = client.SensitiveWordsRecognition(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
