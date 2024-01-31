from typing import Optional

from pydantic import BaseModel


class CompensationSchema(BaseModel):
    timestamp: Optional[str]
    employment_type: Optional[str]
    company_name: Optional[str]
    company_size: Optional[str]
    primary_location_country: Optional[str]
    primary_location_city: Optional[str]
    industry_in_company: Optional[str]
    public_or_private_company: Optional[str]
    years_experience_in_industry: Optional[str]
    years_of_experience_in_current_company: Optional[str]
    job_title_in_company: Optional[str]
    job_ladder: Optional[str]
    job_level: Optional[str]
    required_hours_per_week: Optional[str]
    actual_hours_per_week: Optional[str]
    highest_level_of_formal_education_completed: Optional[str]
    total_base_salary_in_2018: Optional[str]
    total_bonus_in_2018: Optional[str]
    total_stock_options_equity_in_2018: Optional[str]
    health_insurance_offered: Optional[str]
    annual_vacation_in_weeks: Optional[str]
    happiness_at_current_position: Optional[str]
    plan_to_resign_in_next_12_months: Optional[str]
    thoughts_about_direction_of_your_industry: Optional[str]
    gender: Optional[str]
    top_skills_for_job_growth_in_industry_over_next_10_years: Optional[str]
    ever_done_a_bootcamp: Optional[str]
    if_bootcamp_was_worth_it: Optional[str]

    class Config:
        orm_mode = True
