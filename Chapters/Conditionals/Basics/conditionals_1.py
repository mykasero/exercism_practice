"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    is_true = False
    temp_cond = 800
    neutron_cond = 500

    if temperature < temp_cond and neutrons_emitted > neutron_cond and temperature * neutrons_emitted < 500000:
        is_true = True

    return is_true


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    efficiency = None

    generated_power = voltage * current
    effi_percentage = (generated_power / theoretical_max_power) * 100

    if effi_percentage >= 80:
        efficiency = 'green'
    elif effi_percentage >= 60 and effi_percentage < 80:
        efficiency = 'orange'
    elif effi_percentage >= 30 and effi_percentage < 60:
        efficiency = 'red'
    elif effi_percentage < 30:
        efficiency = 'black'

    return efficiency


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    status = None

    prod = temperature * neutrons_produced_per_second

    if prod < 0.9 * threshold:
        status = 'LOW'

    elif prod >= 0.9 * threshold and prod <= 1.1 * threshold:
        status = 'NORMAL'

    else:
        status = 'DANGER'

    return status
