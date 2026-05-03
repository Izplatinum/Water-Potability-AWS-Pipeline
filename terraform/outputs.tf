output "rds_endpoint" {
  value = aws_db_instance.water_postgres.address
}

output "rds_database" {
  value = aws_db_instance.water_postgres.db_name
}

output "rds_username" {
  value = aws_db_instance.water_postgres.username
}

output "rds_password" {
  value     = random_password.db_password.result
  sensitive = true
}
