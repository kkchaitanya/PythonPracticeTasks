from collections import defaultdict
from datetime import datetime 


def monthly_summary(expenses,month, year,logger=None):
    try:
        total = 0
        for expense in expenses:
            exp_year, exp_month, _ = str(expense["date"]).split("-")
            if exp_year == str(year) and exp_month == str(month):
                total += expense["amount"]
        logger.info("Monthly summary generated")
        return total
    except Exception as ex:
        logger.error(f" monthly_summary exception {ex}")

def category_summary(expenses,logger=None):
    try:
        categories = defaultdict(float)
        for expense in expenses:
            categories[expense["category"]] += expense["amount"]
        logger.info("Category summary generated")
        return dict(categories)
    except Exception as ex:
            logger.error(f" monthly_summary exception {ex}")

def highest_expense(expenses,logger=None):
    try:
        if not expenses:
            return None
        highest = max(expenses, key=lambda x: x["amount"])
        logger.info("Highest expense fetched")
        return highest
    except Exception as ex:
        logger.error(f" monthly_summary exception {ex}")

def export_report(expenses,month, year,logger=None):
    try:
        total = monthly_summary(expenses,month, year,logger)
        print(f"total: {total}")
        categories = category_summary(expenses,logger)
        print(f"categorie: {categories}")
        highest = highest_expense(expenses,logger)
        print(f"highest: {highest}")
        now = datetime.now()
        formatted = now.strftime("%d_%m_%Y_%H_%M_%S")
        print(f"formatted: {formatted}")
        report_file = f"reports/report_{formatted}.txt"
        print(f"report_file {report_file}")
        with open(report_file, "w") as file:
            file.write("MONTHLY EXPENSE REPORT\n")
            file.write("=" * 30 + "\n\n")
            file.write(f"Month: {month} Year: {year}\n")
            file.write(f"Total Expense: {total} \n\n")
            file.write("CATEGORY SUMMARY \n")
            file.write("-" * 20 + "\n")
            for category, amount in categories.items():
                file.write(f"{category}: {amount}\n")
                file.write("\n")
            if highest:
                file.write("HIGHEST EXPENSE\n")
                file.write("-" * 20 + "\n")
                file.write(f"Date: {highest['date']}\n")
                file.write(f"Category: {highest['category']}\n")
                file.write(f"Amount: {highest['amount']}\n")
                file.write(f"Description: {highest['description']}\n")
        logger.info(f"Report exported to {report_file}")
        return report_file
    except Exception as ex:
        logger.error(f"Exception in report {ex}")