from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render

def fm_formulas(request):
    flashcards = [
        {
            "term": "Annuity Immediate",
            "definition": "a_n = \\sum_{k=1}^n v^k = \\frac{1 - v^n}{i}"
        },
        {
            "term": "Annuity Due",
            "definition": "\\ddot{a}_n = \\sum_{k=0}^{n-1} v^k = \\frac{1 - v^n}{d}"
        },
        {
            "term": "Perpetuity Immediate",
            "definition": "a_\\infty = \\sum_{k=1}^\\infty v^k = \\frac{1}{i}"
        },
        {
            "term": "Perpetuity Due",
            "definition": "\\ddot{a}_\\infty = \\sum_{k=0}^\\infty v^k = \\frac{1}{d}"
        },
        {
            "term": "Accumulation Function",
            "definition": "a(t) = (1 + i)^t"
        },
        {
            "term": "Force of Interest",
            "definition": "\\delta_t = \\frac{a'(t)}{a(t)}"
        },
        {
            "term": "Effective Interest Rate",
            "definition": "i = e^\\delta - 1"
        },
        {
            "term": "Discount Function",
            "definition": "v = \\frac{1}{1 + i}"
        },
        {
            "term": "Nominal Interest Rate (m compounding periods)",
            "definition": "i^{(m)} = m \\left( (1+i)^{1/m} - 1 \\right)"
        },
        {
            "term": "Accumulated Value of Annuity Due",
            "definition": "s_{\\ddot{a}_n} = \\frac{(1 + i)^n - 1}{d}"
        },
    ]
    return render(request, 'FM_formulas.html', {'flashcards': flashcards})

