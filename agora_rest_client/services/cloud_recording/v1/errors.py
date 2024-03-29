"""
错误码和响应状态码

官方文档: https://doc.shengwang.cn/api-ref/cloud-recording/restful/response-code

错误码
    当调用云端录制 RESTful API 响应码不为 200 时，响应 Body 中会包含一个错误码。

    2：参数不合法，请确保参数类型、大小写和取值范围正确，且必填的参数均已填写。

    7：录制已经在进行中 ，请勿用同一个 Resource ID 重复 start 请求。

    8：HTTP 请求头部字段错误，有以下几种情况：
        Content-type 错误，请确保 Content-type 为 application/json;charset=utf-8。
        请求 URL 中缺少 cloud_recording 字段。
        使用了错误的 HTTP 方法。
        请求包体不是合法的 JSON 格式。

    49：使用同一个 Resource ID 和录制 ID (sid) 重复 stop 请求。

    53：录制已经在进行中。当采用相同参数再次调用 acquire 获得新的 Resource ID，并用于 start 请求时，会发生该错误。如需发起多路录制，需要在 acquire 方法中填入不同的 UID。

    62：如果调用 acquire 请求时出现该错误，则表示你填入的 App ID 没有开通云端录制服务。如果调用 start 请求时出现该错误，则表示由于网络原因没有连接到录制服务，请重新发起请求。

    65：多为网络抖动引起。当调用 start 方法收到该错误码时，需要使用同一 Resource ID 再次调用 start。建议使用退避策略重试两次，如第一次等待 3 秒后重试、第二次等待 6 秒后重试。

    109：加入 RTC 频道的鉴权 Token 过期，你需要获取新的 Token。

    110：加入 RTC 频道的鉴权 Token 错误，你需要确认你是否获取了正确的 Token。

    432：请求参数错误。请求参数不合法，或请求中的 App ID，频道名或用户 ID 与 Resource ID 不匹配。

    433：Resource ID 过期。获得 Resource ID 后必须在 5 分钟内开始云端录制。请重新调用 acquire 获取新的 Resource ID。

    435：没有录制文件产生。频道内没有用户发流，无录制对象。

    501：录制服务正在退出。该错误可能在调用了 stop 方法后再调用 query 时发生。

    1001：Resource ID 解密失败。请重新调用 acquire 获取新的 Resource ID。

    1003：App ID 或者录制 ID（sid）与 Resource ID 不匹配。请确保在一个录制周期内 Resource ID、App ID 和录制 ID 一一对应。

    1013：频道名不合法。频道名必须为长度在 64 字节以内的字符串。以下为支持的字符集范围（共 89 个字符）：
        26 个小写英文字母 a-z
        26 个大写英文字母 A-Z
        10 个数字 0-9
        空格
        "!"、"#"、"$"、"%"、"&"、"("、")"、"+"、"-"、":"、";"、"<"、"="、"."、">"、"?"、"@"、"["、"]"、"^"、"_"、"、"、"|"、"~"、","

    1028：updateLayout 方法的请求包体中参数错误。

    "invalid appid"：无效的 App ID。请确保 App ID 填写正确。如果你已经确认 App ID 填写正确，但仍出现该错误，请联系技术支持。

    "no Route matched with those values"：该错误可能由 HTTP 方法填写错误导致，例如将 GET 方法填写为 POST；也可能由请求 URL 填写错误导致。

    "Invalid authentication credentials"：该错误可能由以下原因导致。如果你已经排除以下原因，但仍出现该错误，请联系联系技术支持。
        客户 ID 或客户密钥填写错误。
        App ID 没有开通云端录制服务。
        HTTP 请求头的认证信息有误，如 Authorization 字段的值 Basic <Authorization> 缺少 Basic。
        HTTP 请求头的格式不正确，如 Content-type 字段的值 application/json;charset=utf-8 大小写不正确或包含空格。


响应状态码
    状态码                     描述
    200                       请求成功。
    201                       录制已经在进行中 ，请勿用同一个 Resource ID 重复 start 请求。
    206                       整个录制过程中没有用户发流，或部分录制文件没有上传到第三方云存储，或录制进程还未结束。
    400                       请求的语法错误（如参数错误）。如果你填入的 App ID 没有开通云端录制服务，也会返回 400。
    401                       未经授权的（客户 ID/客户密钥匹配错误）。
    404                       服务器无法根据请求找到资源（网页）。
    500                       服务器内部错误，无法完成请求。
    504                       服务器内部错误。充当网关或代理的服务器未从远端服务器获取请求。


服务状态
    状态                           描述
    "serviceIdle"                 子模块服务未开始。
    "serviceStarted"              子模块服务已开始。
    "serviceReady"                子模块服务已就绪。
    "serviceInProgress"           子模块服务正在进行中。
    "serviceCompleted"            订阅内容已全部上传至扩展服务。
    "servicePartialCompleted"     订阅内容部分上传至扩展服务。
    "serviceValidationFailed"     扩展服务验证失败。例如 extensionServiceConfig 中 apiData 填写错误。
    "serviceAbnormal"             子模块状态异常。
"""