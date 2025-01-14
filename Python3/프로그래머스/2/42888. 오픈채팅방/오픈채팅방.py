def solution(record):
    message_log = []
    user_info = {}

    for entry in record:
        parts = entry.split()
        actions = parts[0]
        user_id = parts[1]

        if actions == "Enter":
            nickname = parts[2]
            user_info[user_id] = nickname
            message_log.append((user_id, "님이 들어왔습니다."))
        elif actions == "Leave":
            message_log.append((user_id, "님이 나갔습니다."))
        elif actions == "Change":
            nickname = parts[2]
            user_info[user_id] = nickname

    final_messages = []

    for user_id, message in message_log:
        final_messages.append(user_info[user_id] + message)

    return final_messages