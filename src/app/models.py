from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Compensation(Base):
    __tablename__ = "compensations"  # noqa

    id = Column(BigInteger, primary_key=True, index=True)
    timestamp = Column(BigInteger)
    employment_type = Column(String)
    company_name = Column(String)
    company_size = Column(String)
    primary_location_country = Column(String)
    primary_location_city = Column(String)
    industry_in_company = Column(String)
    public_or_private_company = Column(String)
    years_experience_in_industry = Column(String)
    years_of_experience_in_current_company = Column(String)
    job_title_in_company = Column(String)
    job_ladder = Column(String)
    job_level = Column(String)
    required_hours_per_week = Column(Integer)
    actual_hours_per_week = Column(Integer)
    highest_level_of_formal_education_completed = Column(String)
    total_base_salary_in_2018 = Column(BigInteger)
    total_bonus_in_2018 = Column(BigInteger)
    total_stock_options_equity_in_2018 = Column(BigInteger)
    health_insurance_offered = Column(String)
    annual_vacation_in_weeks = Column(BigInteger)
    happiness_at_current_position = Column(String)
    plan_to_resign_in_next_12_months = Column(String)
    thoughts_about_direction_of_your_industry = Column(String)
    gender = Column(String)
    top_skills_for_job_growth_in_industry_over_next_10_years = Column(String)
    ever_done_a_bootcamp = Column(String)
    if_bootcamp_was_worth_it = Column(String)
