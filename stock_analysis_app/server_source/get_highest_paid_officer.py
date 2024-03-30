def get_highest_paid_officer(officers_list):
    """
    Function to get information about the highest paid officer
    """
    highest_paid = max(officers_list, key=lambda officer: officer.get("totalPay", 0))
    return (
        highest_paid["title"],
        highest_paid["name"],
        highest_paid["totalPay"],
    )
