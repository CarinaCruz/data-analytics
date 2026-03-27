import os

# Simple.SQL generator and validator stub.
# Replace generation with a real LLM integration (openai) when ready.

def generate_sql(prompt: str):
    low = prompt.lower()
    if "vendas por mês" in low or "vendas por mes" in low or "sales per month" in low:
        sql = (
            "SELECT DATE_FORMAT(o.order_date, '%Y-%m') AS month, "
            "SUM(oi.quantity * oi.unit_price) AS total_sales "
            "FROM orders o JOIN order_items oi ON o.id=oi.order_id "
            "WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH) "
            "GROUP BY month ORDER BY month;"
        )
        explanation = "Agrega vendas por mês nos últimos 6 meses a partir das tabelas orders e order_items."
        return sql, explanation
    # fallback
    return "SELECT 1;", "Fallback SQL: não foi possível inferir uma query detalhada a partir do prompt." 


def validate_sql(sql: str):
    """Retorna lista de problemas (vazia se ok). Regras simples para evitar queries perigosas."""
    forbidden_tokens = ["drop ", "delete ", "truncate ", "alter ", "shutdown", ";--", "/*"]
    issues = []
    low = sql.lower()
    for t in forbidden_tokens:
        if t in low:
            issues.append(f"Token proibido detectado: {t.strip()}")
    # Detect multiple statements (basic)
    if low.count(";") > 1:
        issues.append("Múltiplas instruções SQL detectadas. Permitido apenas uma SELECT.")
    # Allow only SELECT statements
    if not low.strip().startswith("select"):
        issues.append("Apenas consultas SELECT são permitidas pelo endpoint.")
    return issues
