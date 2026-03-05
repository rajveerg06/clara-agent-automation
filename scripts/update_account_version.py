from version_manager import save_version


def update_account(account_id, old_memo, updates, agent_generator):

    # copy v1 memo
    updated_memo = old_memo.copy()

    # apply onboarding updates
    for key, value in updates.items():
        updated_memo[key] = value

    # generate new agent spec
    updated_agent = agent_generator(updated_memo)

    # save version v2
    save_version(account_id, "v2", updated_memo, updated_agent)

    return updated_memo